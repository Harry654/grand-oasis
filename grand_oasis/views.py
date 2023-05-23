from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Sum
from datetime import date, datetime
today = date.today()

def index(request):
    context = {
        "num_of_rooms": len(Room.objects.all()),
        "num_of_clients": len(User.objects.filter(is_staff=False)),
        "num_of_staff": len(User.objects.filter(is_staff=True)),
        }
    return render(request, 'index.html', context)

def rooms(request):
    message = ""
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # set the room being booked to unavailable
            roomID = request.POST['room']
            currentRoom = Room.objects.get(id=roomID)
            currentRoom.is_available = False

            # save reservation
            form.save()

            # update the room
            currentRoom.save()
            message = f"Room {currentRoom.room_number} {currentRoom.category} has been booked"
            # return redirect('rooms')
        else:
            print(form.errors)
    else:
        form = ReservationForm()

    # get rooms for each floor
    floor1 = Room.objects.filter(floor_number=1)
    floor2 = Room.objects.filter(floor_number=2)
    floor3 = Room.objects.filter(floor_number=3)

    context = {
        "floors": [floor1, floor2, floor3], 
        'form': form, 
        'rooms': Room.objects.all(), 
        'user': request.user,
        'reservations': Reservation.objects.all(),
        'users': User.objects.all(),
        "message": message
        # 'extra_services': ExtraService.objects.all()
    }
    return render(request, 'rooms.html', context)

def myBookings(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.user.is_staff:
        return redirect('admin')
    
    message = ""
    if request.method == 'POST':
        if 'add_service' in request.POST:
            service_date_time = request.POST['service_date_time']

            service = ServiceType.objects.get(id=request.POST['service_id'])
            reservation = Reservation.objects.get(id=request.POST['reservation_id'])
            extra_service = ExtraService.objects.create(reservation=reservation, service=service)
            extra_service.save()
            
            new_extra_service = ExtraService.objects.get(reservation__id=request.POST['reservation_id'], service__id=request.POST['service_id'])

            service_date = ServiceDate.objects.create(extra_service=new_extra_service, service_date_time=service_date_time)
            # form = DateForm(service_date)
            service_date.save()

            # reservation = Reservation.objects.get(id=request.POST['reservation_id'])
            reservation.total_price = reservation.total_price + service.price
            reservation.save()
            # print(reservation.total_price + service.price)

        elif 'renew_reservation' in request.POST:
            print("renew_reservation")

            new_checkout = datetime.strptime(request.POST['new_checkout'], '%Y-%m-%d').date()

            current_reservation = Reservation.objects.get(id=request.POST['reservation_id'])
            
            prev_duration = (current_reservation.checkout - current_reservation.checkin).days
            new_duration = (new_checkout - current_reservation.checkin).days

            current_reservation.checkout = new_checkout

            current_reservation.total_price = current_reservation.total_price - (prev_duration*current_reservation.room.price_per_night)
            current_reservation.total_price = current_reservation.total_price + (new_duration*current_reservation.room.price_per_night)
            # current_reservation.duration = new_duration

            print(request.POST['new_checkout'])
            print(current_reservation.checkout)
            current_reservation.save()

            message = "Checkout updated successfully"
        elif 'delete_reservation' in request.POST:
            reservation = Reservation.objects.get(id=request.POST['reservation_id'])
            reservation.delete()
            message = f"Your reservation for {reservation.room.room_number} {reservation.room.category} has been cancelled"
    else:
        form = DateForm()

    context = {
        'myReservations': Reservation.objects.filter(user__id=request.user.id),
        'serviceDates': ServiceDate.objects.all(),
        # 'serviceDates': ServiceDate.objects.filter(extra_service__reservation__user__id=request.user.id),
        'serviceTypes': ServiceType.objects.all(),
        'form': DateForm(),
        "message": message,
        "messages": Contact.objects.all(),
        "today": today,
    }
    return render(request, 'my-bookings.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if (user.is_staff):
                return redirect('admin')
            return redirect('myBookings')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        new_user = User.objects.create(username=request.POST['username'], email=request.POST['email'])
        new_user.set_password(request.POST['password'])
        new_user.save()

        return redirect('login')

    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def admin(request):
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    if not request.user.is_staff:
        return redirect('rooms')
    
    message = ""
    if request.method == 'POST':
        if 'delete_reservation' in request.POST:
            current_reservation = Reservation.objects.get(id=request.POST['reservation_id'])
            current_reservation.delete()
        elif 'reply_message' in request.POST:
            current_message_sender = User.objects.get(id=request.POST['msg_sender'])
            current_message_receiver = User.objects.get(id=request.POST['msg_receiver'])
            new_message = Contact.objects.create(
                msg_sender = current_message_sender,
                msg_receiver = current_message_receiver,
                subject = request.POST['subject'],
                message = request.POST['message'],
            )
            new_message.save()

            message = "Response sent"
        elif 'delete_user' in request.POST:
            current_user = User.objects.get(id=request.POST['user_id'])
            current_user.delete()
            message = "User deleted successfully"
        elif 'update_user' in request.POST:
            current_user = User.objects.get(id=request.POST['user_id'])
            current_user.username = request.POST['username']
            current_user.email = request.POST['email']
            current_user.save()

            message = "User updated successfully"
        elif 'make_reservation' in request.POST:
            form = ReservationForm(request.POST)
            if form.is_valid():
                # set the room being booked to unavailable
                roomID = request.POST['room']
                currentRoom = Room.objects.get(id=roomID)
                currentRoom.is_available = False

                # save reservation
                form.save()

                # update the room
                currentRoom.save()
                message = f"Room {currentRoom.room_number} {currentRoom.category} has been booked"
                # return redirect('rooms')
            else:
                print(form.errors)

            message = "Room booked successfully"
        elif 'add_user' in request.POST:
            is_staff = True if request.POST['user_type'] == 'admin' else False
            new_user = User.objects.create(username=request.POST['username'], email=request.POST['email'], is_staff=is_staff)
            new_user.set_password(request.POST['password'])
            new_user.save()

            message = "User Created successfully"

    # print(Reservation.objects.filter(date_booked=today)
    start_of_day = datetime.combine(today, datetime.min.time())
    end_of_day = datetime.combine(today, datetime.max.time())

    total_price_today = Reservation.objects.filter(date_booked__range=(start_of_day, end_of_day)).aggregate(Sum('total_price'))['total_price__sum']

    if total_price_today is None:
        total_price_today = 0

    bookings_today = Reservation.objects.filter(date_booked__range=(start_of_day, end_of_day))

    if bookings_today is None:
        bookings_today = 0

    total_clients = User.objects.filter(is_staff=False)
    total_rooms = Room.objects.all()

    floor1 = Room.objects.filter(floor_number=1, is_available=True)
    floor2 = Room.objects.filter(floor_number=2, is_available=True)
    floor3 = Room.objects.filter(floor_number=3, is_available=True)

    context = {
        "floors": [floor1, floor2, floor3], 
        'user': request.user, 
        "message": message, 
        "reservations": Reservation.objects.all(),
        "users": User.objects.all(),
        "messages": Contact.objects.all(),
        "users": User.objects.all(),
        "available_rooms": Room.objects.filter(is_available=True),
        'total_price_today': total_price_today,
        'bookings_today': len(bookings_today),
        'total_clients': len(total_clients),
        'total_rooms': len(total_rooms),
        "rooms": Room.objects.all()
    }
    return render(request, 'admin.html', context)

def contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.user.is_staff:
        return redirect('admin')
    
    message = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "Message logged successfully"
            form.save()

            return redirect('contact')
        else:
            message = "Something went wrong"
    else:
        form = ContactForm()

    context = {'user': request.user, "message": message}
    return render(request, 'contact.html', context)

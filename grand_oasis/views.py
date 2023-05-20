from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html', {"num_of_rooms": len(RoomModel.objects.all())})


def rooms(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # set the room being booked to unavailable
            roomID = request.POST['room']
            currentRoom = RoomModel.objects.get(id=roomID)
            currentRoom.is_available = False

            # update the room
            currentRoom.save()

            # save reservation
            form.save()

            return redirect('rooms')
    else:
        form = ReservationForm()

    # get rooms for each floor
    floor1 = RoomModel.objects.filter(floor_number=1)
    floor2 = RoomModel.objects.filter(floor_number=2)
    floor3 = RoomModel.objects.filter(floor_number=3)

    context = {
        "floors": [floor1, floor2, floor3], 
        'form': form, 
        'rooms': RoomModel.objects.all(), 
        'reservations': ReservationModel.objects.all(),
        'user': request.user
    }
    return render(request, 'rooms.html', context)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('rooms')  # Redirect to a success page
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')
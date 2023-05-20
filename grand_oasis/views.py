from django.shortcuts import render, redirect
from .models import *
from .forms import *


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('register')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(request)
            # form.save()

            return redirect('login')
    else:
        form = LoginForm()

    context = {'form': form, 'error': error}
    return render(request, 'login.html', context)


def index(request):
    return render(request, 'index.html', {"num_of_rooms": len(RoomModel.objects.all())})


def rooms(request):
    if request.method == 'POST':
        # print(request.POST['checkin'])
        # print(request.POST['checkout'])
        # print(request.POST['room'])
        form = ReservationForm(request.POST)
        if form.is_valid():
            print(form)

            # set the room to unavailable
            roomID = request.POST['room']
            currentRoom = RoomModel.objects.get(id=roomID)
            currentRoom.is_available = False

            # save reservation
            form.save()
            
            # update the room
            currentRoom.save()
            
            return redirect('rooms')
        else:
            print("rf")
    else:
        form = ReservationForm()

    floor1 = RoomModel.objects.filter(floor_number=1)
    floor2 = RoomModel.objects.filter(floor_number=2)
    floor3 = RoomModel.objects.filter(floor_number=3)
    return render(request, 'rooms.html', {"floors": [floor1, floor2, floor3], 'form': form, 'rooms': RoomModel.objects.all()})

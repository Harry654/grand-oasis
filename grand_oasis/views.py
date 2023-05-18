from django.shortcuts import render
from .models import RoomModel
def index(request):
    return render(request, 'index.html')

def rooms(request):
    floor1 = RoomModel.objects.filter(floor_number=1)
    floor2 = RoomModel.objects.filter(floor_number=2)
    floor3 = RoomModel.objects.filter(floor_number=3)
    return render(request, 'rooms.html', { "floor1": floor1, "floor2": floor2, "floor3": floor3 })

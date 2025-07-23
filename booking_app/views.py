from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from booking_app.models import *

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(
        request,
        "rooms.html",
        context=context
    )

def room_detail(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(
        request,
        "room.html",
        context=context
    )

@login_required
def create_room(request):
    if request.method == 'POST':
        hotel = request.POST.get('hotel')
        room_number = request.POST.get('room_number')
        description = request.POST.get('description')
        capacity = request.POST.get('capacity')
        cost_per_day = request.POST.get('cost_per_day')
        all_inclusive = request.POST.get('all_inclusive') == 'on'

        Room.objects.create(
            hotel=hotel,
            room_number=int(room_number),
            description=description,
            capacity=int(capacity),
            cost_per_day=float(cost_per_day),
            all_inclusive=all_inclusive
        )
        return redirect('room_list')
    return render(
        request,
        "create_room.html"
    )

def intro(request):
    return render(
        request,
        "intro.html"
    )
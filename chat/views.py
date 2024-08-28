from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'salas.html',{
    'rooms':rooms
        })



@login_required
def room(request, room_id):
    try:
        room = request.user.rooms_joined.get(id=room_id)

    except Room.DoesNotExist:
        error = '403 No puedes acceder a este chat'
        return render(request, 'salas.html', {'error':error, 'rooms':Room.objects.all()})

    return render(request, 'room.html', {'room':room})


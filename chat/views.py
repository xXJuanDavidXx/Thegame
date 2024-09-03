from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Mensajes
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import RoomForm, RoomRequestForm
from django.contrib.auth.models import User


# Create your views here.

###Lista las salas disponibles en la base de datos.
@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'salas.html',{
    'rooms':rooms
        })


###accede a la sala o da un mensaje de error en caso de no pertenecer.
@login_required
def room(request, room_id):
    try:
        room = request.user.rooms_joined.get(id=room_id)
    except Room.DoesNotExist:
        error = '403 No puedes acceder a este chat'
        return render(request, 'salas.html', {'error': error, 'rooms': Room.objects.all()})

    mensajes = Mensajes.objects.filter(room=room).order_by('tiempo')
    return render(request, 'room.html', {'room': room, 'mensajes': mensajes})




######################################################################################################

#####Crear una room####
@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.creador = request.user
            room.save()
            return redirect('home')
    else:
        form = RoomForm()
    return render(request, 'SalasCreadas.html', {'form': form})



##### La vista que procesa la union a la sala. ####
@login_required
def request_to_join(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.pendientes.add(request.user)
    return redirect('home')


####La vista para manejar las peticiones de unirse a la sala.#####
@login_required
def manage_requests(request, room_id):
    room = get_object_or_404(Room, id=room_id, creador=request.user)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = get_object_or_404(User, id=user_id)
        if action == 'accept':
            room.users.add(user)
            room.pendientes.remove(user)
        elif action == 'reject':
            room.pendientes.remove(user)
        return redirect('mis_salas')
    return render(request, 'ManejarPeticiones.html', {'room': room, 'requests': room.pendientes.all()})



#### Vista que me permite administrar las salas por usuario ###

@login_required
def mis_salas(request):
    rooms = Room.objects.filter(creador=request.user)
    return render(request, 'mis_salas.html', {
        'rooms': rooms,
    })






















from django.shortcuts import render, redirect, get_object_or_404 #para redireccionar al usuario
from django.http import HttpResponse,HttpResponseRedirect #para poder hacer una respuesta http
from .models import Consola, JuegoIndie, Profile
from django.views.generic import TemplateView 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Importamos esto para crear el apartado de registro y loggeo
from django.contrib.auth.models import User # importamos esto para guardar los datos pasados por el usuario y registrarlos en el modelo usuario de Django
from django.contrib.auth import authenticate, login, logout # Para crear la cookie de usuario y para poder cerrar sesión
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import GameForm


# Create your views here.


#-----Principal------

#---pagina principal

def index(request):
    return render(request, 'index.html')

#---pagina de registro

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tu')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})



#---pagina de loggeo

def registro(request):
    if request.method == 'GET':                   #validamos que la solicitud sea get para mostrar el login
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:                                         #aquí verificamos que el usuario y contraseña exista
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                "error": 'Usuario o contraseña incorrecta'   #va a devolver si no existe..
            })
        else:
            login(request, user) #si el usuario y contraseña son correctos, iniciamos la cookie de sesión
            return redirect('tu')


        
        




#---cerrar sesión
def singout(request):
    logout(request)
    return redirect('index')

#---pagina del usuario---
@login_required ##hace solo accesible a usuarios con sesión, si no los re dirige al login
def tu(request):
    return render(request,'me.html')

    
def editar(request):
    return HttpResponse('ola') 



#___Pagina para subir los indie---

@login_required
def indie(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            # Validar que el archivo sea .zip
            archivo = request.FILES.get('archivo')
            if not archivo.name.endswith('.zip'):
                form.add_error('archivo', 'Por favor sube un archivo ZIP.')
                return render(request, 'SubirJuego.html', {'form': form})

            # Guardar los datos del juego y la imagen (si se proporcionó)
            juego_indie = form.save(commit=False)
            juego_indie.desarrollador = request.user  # Establece el desarrollador que sube el juego
            if 'img' in request.FILES:
                juego_indie.img = request.FILES['img']
            juego_indie.save()
            return HttpResponseRedirect('tu')  # Redirige a la página 'tu' después de guardar el juego
    else:
        form = GameForm()

    return render(request, 'SubirJuego.html', {'form': form})

#----Apartado de juegos subidos por el usuario.
#@login_required
def mis_juegos(request):
    juegos_usuario = JuegoIndie.objects.filter(desarrollador=request.user)
    return render(request, 'mis_juegos.html', {'juegos_usuario': juegos_usuario})







# ------- Parte de juegos retro sin registro de usuario. -------



def categorias(request):
    return render(request, 'categorias.html')

def soporte(request):
    return render(request,'soporte.html')

def ayuda(request):
    return render(request, 'help.html')





#def hola(request, username):
 #   print(username)
 #   return HttpResponse("<h1>THEGAME {}</h1>".format(username)) #Lo que estamos haciendo aqui es concatenar el parametro que se espera recibir en el HttpResponse 


def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    c = Consola.objects.get(id=kwargs['id'])
    return HttpResponse("La consola es {}".format(c.consola))



















#class About(TemplateView):
#    template_name = "Carlist.html"
#
#
#    def get_context_data(self):
#        car_list = [
#        {"title": "BMW"},
#        {"title": "Mazda"}
#                ]
#        return {
#        "car_list": car_list
#                }






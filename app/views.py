from django.shortcuts import render, redirect, get_object_or_404 #para redireccionar al usuario
from django.http import HttpResponse,HttpResponseRedirect #para poder hacer una respuesta http
from .models import Consola, JuegoIndie, Profile, Juego
from django.views.generic import TemplateView 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Importamos esto para crear el apartado de registro y loggeo
from django.contrib.auth.models import User # importamos esto para guardar los datos pasados por el usuario y registrarlos en el modelo usuario de Django
from django.contrib.auth import authenticate, login, logout # Para crear la cookie de usuario y para poder cerrar sesión
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import GameForm, Profile_img #organizar en la app usuarios
from django.contrib import messages
from juegos.models import GamesWeb

# Create your views here.


#-----Principal------

#---pagina principal

def index(request):
    return render(request, 'index.html')


def search_view(request):
    query = request.GET.get('q')  #q es el nombre que le puse al input que vamos a recibir
    if query:
        results = Juego.objects.filter(titulo__icontains=query) 
    else:
        results = Juego.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})
    


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

            # Guardar los datos del juego y la imagen principal (si se proporcionó)
            juego_indie = form.save(commit=False)
            juego_indie.desarrollador = request.user  # Establece el desarrollador que sube el juego
            juego_indie.save()
            return redirect('mis_juegos')  # Redirige a la página 'tu' después de guardar el juego
    else:
        form = GameForm()

    return render(request, 'SubirJuego.html', {'form': form})

#----Apartado de juegos subidos por el usuario.
#@login_required
def mis_juegos(request):
    juegos_usuario = JuegoIndie.objects.filter(desarrollador=request.user)
    juegos_web = GamesWeb.objects.filter(usuario=request.user)
    return render(request, 'mis_juegos.html', {
        'juegos_usuario': juegos_usuario,
        'juegos_web': juegos_web,
        })


def lista_indie(request):
    
    juegos = JuegoIndie.objects.all().prefetch_related('imagenes')
    context = {
        'juegos': juegos
            }

    return render(request, 'Indie.html', context)










# ------- Parte de juegos retro sin registro de usuario. -------



def categorias(request):
    consolas = Consola.objects.all()
    context = {
        'consolas': consolas,
        'current_page': 'categorias'
    }
    return render(request, 'categorias.html', context)

##-----Juego por consola-----

def juegos_por_consola(request, consola_id):
    consola = get_object_or_404(Consola, id=consola_id)
    juegos = Juego.objects.filter(consola=consola)
    context = {
        'consola': consola,
        'juegos': juegos
    }
    return render(request, 'juegos_por_consola.html', context)






###---------


def soporte(request):
    return render(request,'soporte.html')

def ayuda(request):
    return render(request, 'help.html')





#def hola(request, username):
 #   print(username)
 #   return HttpResponse("<h1>THEGAME {}</h1>".format(username)) #Lo que estamos haciendo aqui es concatenar el parametro que se espera recibir en el HttpResponse 


### Web o descarga ###
def webOzip(request):
    return render(request, 'webOzip.html')
    






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






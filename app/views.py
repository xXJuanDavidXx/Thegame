from django.shortcuts import render, redirect #para redireccionar al usuario
from django.http import HttpResponse #para poder hacer una respuesta http
from .models import Consola
from django.views.generic import TemplateView 
from django.contrib.auth.forms import UserCreationForm # Importamos esto para crear el apartado de login
from django.contrib.auth.models import User # importamos esto para guardar los datos pasados por el usuario y registrarlos en el modelo usuario de Django
from django.contrib.auth import authenticate, login, logout # Para crear la cookie de usuario y para poder cerrar sesión
from django.db import IntegrityError

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



#---pagina de loggeo el usuario y cerrar sesión--

def registro(request):
    return render(request,'login.html')

def singout(request):
    logout(request)
    return redirect('index')

def tu(request):
    return render(request,'me.html')



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






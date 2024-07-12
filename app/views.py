from django.shortcuts import render
from django.http import HttpResponse #para poder hacer una respuesta http
from .models import Consola
from django.views.generic import TemplateView 
from django.contrib.auth.forms import UserCreationForm # Importamos esto para crear el apartado de login
from django.contrib.auth.models import User # importamos esto para guardar los datos pasados por el usuario y registrarlos en el modelo usuario de Django
# Create your views here.


#-----Principal------

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        # Renderizar el formulario de registro cuando la solicitud es GET
        return render(request, 'signup.html', {
            'form': UserCreationForm()  # Llamar al formulario de creación de usuario
        })
    
    # Procesamiento de los datos cuando la solicitud es POST
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Crear un nuevo usuario con el nombre de usuario y la contraseña proporcionados
                usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                usuario.save()  # Guardar el usuario en la base de datos
                return HttpResponse('Usuario creado')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),  # Llamar al formulario de creación de usuario
                    'error': 'Usuario existente'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm(),  # Llamar al formulario de creación de usuario
                'error': 'Las contraseñas no coinciden.'
            })




# ------- segunda -------

def categorias(request):
    return render(request, 'categorias.html')

def soporte(request):
    return render(request,'soporte.html')

def ayuda(request):
    return render(request, 'help.html')

def tu(request):
    return render(request, 'me.html')




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






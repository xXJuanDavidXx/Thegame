from django.shortcuts import render

from .models import Consola

# Create your views here.

from django.http import HttpResponse #para poder hacer una respuesta http

def index(request):
    return render(request, 'index.html')



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


    

def about(request):
    return HttpResponse("<h1>mamasita la que lo lea</h1>")

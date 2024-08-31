from django.shortcuts import render, redirect
from .models import GamesWeb
from .forms import JuegoForm
from django.contrib.auth.decorators import login_required




@login_required
def subir_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            juego = form.save(commit=False)
            juego.usuario = request.user
            juego.save()
            return redirect('listajuegos')
    else:
        form = JuegoForm()
    return render(request, 'subir_juegos.html', {'form': form})




def lista_juegos(request):
    juegos = GamesWeb.objects.all()
    return render(request, 'lista_juegos.html', {'juegos': juegos})



def ejecutar_juego(request, juego_id):
    juego = GamesWeb.objects.get(pk=juego_id)
    return render(request, 'ejecutar_juegos.html', {'juego': juego})






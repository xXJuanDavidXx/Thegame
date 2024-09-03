from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from app.forms import Profile_img
from django.contrib import messages
from app.models import Consola, JuegoIndie, Profile, Juego


# Create your views here.


###APARTADO DE LOGIN###
def registro(request):
    if request.method == 'GET':                   #validamos que la solicitud sea get para mostrar el login
        return render(request, 'users/login.html', {
            'form': AuthenticationForm,
            'current_page': 'login'
            })
    else:                                         #aquí verificamos que el usuario y contraseña exista
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/login.html', {
                'form': AuthenticationForm,
                "error": 'Usuario o contraseña incorrecta'   #va a devolver si no existe..
            })
        else:
            login(request, user) #si el usuario y contraseña son correctos, iniciamos la cookie de sesión
            return redirect('tu')



###APARTADO DE SIGNUP




class Register(CreateView):

    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy("index")


    def get_context_data(self, **kwargs):
        """
logout        Agrega `current_page` al contexto para usar en las plantillas.
        """
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'signup'
        return context



    def form_valid(self, form):
        """
        Procesa una validación exitosa del formulario.

        Guarda el nuevo usuario, lo autentica y lo inicia sesión.
        """
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return response





#Logout

def singout(request):
    logout(request)
    return redirect('index')




#Perfil
@login_required
def tu(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    return render(request,'me.html',{'profile':profile, 'user': request.user})








#Editar
@login_required
def editar(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = Profile_img(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            try:
                archivo = request.FILES['profile_picture']
                img_valida = ['.jpg', '.jpeg', '.png', '.gif']
                if not any(archivo.name.lower().endswith(ext) for ext in img_valida):
                    messages.error(request, 'Solo se permiten archivos de imagen con extensiones: .jpg, .jpeg, .png, .gif')
                    return redirect('edit')
            except KeyError:
                # No se subió ninguna nueva imagen, así que no hacemos nada especial aquí.
                pass

            form.save()
            messages.success(request, 'Imagen actualizada correctamente')
            return redirect('edit')
    else:
        form = Profile_img(instance=profile)

    return render(request, 'editar.html', {'form': form, 'profile': profile})




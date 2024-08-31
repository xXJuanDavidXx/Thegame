from django import forms
from .models import GamesWeb

class JuegoForm(forms.ModelForm):
    class Meta:
        model = GamesWeb
        fields = ['nombre', 'descripcion', 'archivo_js', 'imagen']


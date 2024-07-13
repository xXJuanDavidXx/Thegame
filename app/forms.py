from .models import JuegoIndie
from django import forms

class GameForm(forms.ModelForm):
    class Meta:
        model = JuegoIndie
        fields = ['titulo','img', 'descripcion', 'archivo']

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        if archivo:
            if not archivo.name.endswith('.zip'):
                raise forms.ValidationError('Por favor sube un archivo ZIP.')
        return archivo





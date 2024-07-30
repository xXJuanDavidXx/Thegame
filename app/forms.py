from .models import JuegoIndie, Profile
from django import forms

class GameForm(forms.ModelForm):
    class Meta:
        model = JuegoIndie
        fields = ['titulo','img', 'descripcion', 'archivo']


class Profile_img(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']




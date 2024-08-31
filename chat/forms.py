from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'img']



class RoomRequestForm(forms.Form):
    room_id = forms.IntegerField(widget=forms.HiddenInput)







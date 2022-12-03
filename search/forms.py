from django import forms
from .models import Playlist

class SearchForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = '__all__'
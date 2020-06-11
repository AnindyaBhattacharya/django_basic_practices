from django import forms
from . import models

class movie_forms(forms.ModelForm):
    class Meta:
        model=models.MovieDB
        fields="__all__"

from django import forms

class name(forms.Form):
    name = forms.CharField(label="Name")
    roll = forms.IntegerField(label="Roll")
class addr(forms.Form):
    address = forms.CharField(label="Address",widget=forms.Textarea)
    pin = forms.IntegerField(label="PIN")
class contact(forms.Form):
    ph = forms.IntegerField()
    email = forms.CharField(label="E-Mail")

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
def home(request):
    return render(request,"UserAuthApp/home.html")
@login_required
def english(request):
    return render(request,"UserAuthApp/english.html")
@login_required
def reasoning(request):
    return render(request,"UserAuthApp/reasoning.html")
@login_required
def aptitude(request):
    return render(request,"UserAuthApp/aptitude.html")
def logout(request):
    return render(request,"UserAuthApp/logout.html")
'''def signup(request):
    form=forms.SignUpForm()
    if request.method=="POST":
        form=forms.SignUpForm(request.POST)
        print("form ",form)
        print("type of form" ,type(form))
        user=form.save()
        print("user", user)
        print("type of user", type(user))
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect("/accounts/login")
    else :
        return render(request,"UserAuthApp/signup.html",{"form":form})
'''
class Signup(CreateView):
    model=User
    fields=["username","password","first_name","last_name","email"]
    template_name = 'UserAuthApp/signup.html'
    def get_success_url(self):
        return reverse_lazy("home")

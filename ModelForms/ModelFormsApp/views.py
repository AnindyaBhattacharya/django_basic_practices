from django.shortcuts import render
from . import forms,models
# Create your views here.
def index(request):
    return render(request,"ModelForms/index.html")

def add(request):
    form = forms.movie_forms()
    if request.method == "POST":
        form = forms.movie_forms(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,"ModelForms/add.html",{"form":form})

def fetch(request):
    movies_list=models.MovieDB.objects.all().order_by("points")
    print((movies_list))
    print(type(movies_list))
    return render(request,"ModelForms/show.html",{"movies_list":movies_list})

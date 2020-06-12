from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
class SimpleView(View):
    def get(self,request):
        return HttpResponse("<h1>Hello World</h1>")

class TemplateView(TemplateView):
    template_name = 'home.html'
    # passing context parameters
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["name"]="Anindya"
        context["dept"]="Mech"
        context["roll"]=127
        return context              # returning the context dictonary.

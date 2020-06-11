from django.shortcuts import render
from cookieapp.forms import *

# Create your views here.
def name_view(request):
    request.COOKIES.clear()
    form=name()
    return render(request,"cookieapp/name.html",{"form":form})

def address_view(request):
    name = request.POST["name"]
    roll = request.POST["roll"]
    print("-"*50)
    print(type(request.COOKIES))
    print(request.COOKIES)
    print("-"*50)
    form=addr()
    response = render(request,"cookieapp/address.html",{"form":form})
    response.set_cookie("name",name,120)
    response.set_cookie("roll",roll,120)
    return response

def contact_view(request):
    addr = request.POST["address"]
    pin = request.POST["pin"]
    print("*"*50)
    print(type(request.COOKIES))
    print(request.COOKIES)
    print("*"*50)
    form =contact()
    response = render(request,"cookieapp/phone.html",{"form":form})
    response.set_cookie("addr",addr,90)
    response.set_cookie("pin",pin,90)
    return response

def results_view(request):
    name = request.COOKIES["name"]
    pin = request.COOKIES["pin"]
    addr = request.COOKIES["addr"]
    roll = request.COOKIES["roll"]
    phn = request.POST["ph"]
    email = request.POST["email"]
    resp = render(request,"cookieapp/results.html",{"name":name,"addr":addr,"phn":phn,"roll":roll,"pin":pin,"email":email})
    resp.set_cookie("phn",phn,60)
    resp.set_cookie("email",email,60)
    return resp

from django.urls import reverse
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from eStore import urls
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            print("Login success")
            print(request.user)
            return HttpResponsePermanentRedirect(reverse("navigate"))
    print("try again")
    return render(request, 'login.html')

def Login(request):
    if request.user.is_authenticated:
        return HttpResponsePermanentRedirect(reverse("homepage"))
    return HttpResponseRedirect(reverse("index"))



def navigate(request):
    if request.user.is_authenticated:
        return HttpResponsePermanentRedirect(reverse("homepage"))
    return HttpResponseRedirect(reverse("index"))
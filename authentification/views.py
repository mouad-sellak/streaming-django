from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def auth(request):
    return render(request, 'authentification/auth.html',)


def signup(request):
    return render(request, 'authentification/signup.html',)

def signin(request):
    return render(request, 'authentification/signin.html',)

def signout(request):
    pass



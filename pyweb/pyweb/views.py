from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("My homepage : this is the message from httpResponse in 'homepage' View.py")
    # return HttpResponse("this is the homepage")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("My About page : this is the message from httpResponse in 'about' View.py") 
    return render(request,'about.html')
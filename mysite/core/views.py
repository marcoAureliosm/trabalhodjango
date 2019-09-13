from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Alô, Mundo!")
# Create your views here.

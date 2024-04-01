from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ml(request):
    return HttpResponse("<h1>welcome to ml</h1>")
def software(request):
    return HttpResponse("<h1>welcome to software</h1>")
def engineer(request):
    x=10
    y=13
    return HttpResponse(x+y)
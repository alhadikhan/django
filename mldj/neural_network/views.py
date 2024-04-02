from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def neural(request):
    return HttpResponse("This is the neural_network app")
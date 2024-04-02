from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dpl(request):
    return HttpResponse("This is the deeplearning app")
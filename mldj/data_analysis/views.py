from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def da(request):
    return HttpResponse("This is the data_analysis app")
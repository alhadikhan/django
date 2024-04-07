from django.shortcuts import render
# Create your views here.
def neural(request):
    return render(request,"nn/neural_network.html")
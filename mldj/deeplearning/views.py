from django.shortcuts import render
# Create your views here.
def dpl(request):
    return render(request,"dp/deeplearning.html")
from django.shortcuts import render
# Create your views here.
def da(request):
    return render(request,"data_analysis.html")
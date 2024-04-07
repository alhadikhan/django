from django.shortcuts import render
# Create your views here.
def da(request):
    return render(request,"da/data_analysis.html")
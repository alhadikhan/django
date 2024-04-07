from django.shortcuts import render
# Create your views here.
def ml(request):
    return render(request,"ml/ml.html")
def software(request):
    return render(request,"ml/sft.html")
def ds(request):
    return render(request,"ml/ds.html")
from django.shortcuts import render
# Create your views here.
def ml(request):
    return render(request,"ml/ml.html")
def software(request):
    return render(request,"ml/sft.html")
def ds(request):
    times=100
    number=123
    sc='scientist'
    math="Mathematics"
    grt={'x':times,'y':number,'s':sc,'m':math}
    return render(request,"ml/ds.html",context=grt)
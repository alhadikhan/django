from django.urls import path
from . import views
urlpatterns = [
    path('machine/',views.ml),
  #  path('sft/',views.software),
   # path("add/",views.engineer),
  
]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.ml),
    path('sft/',views.software),
    path("add/",views.engineer),
  
]

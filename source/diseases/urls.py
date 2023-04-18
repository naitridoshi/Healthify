from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.home),
    path('parkinsons/' , views.parkinsonsPage , name='vparkinsons'),
    path('breastCancer/', views.breastCancerPage, name='vbreastCancer'),
    path('diabetes/' , views.diabetesPage , name='vdiabetes'),
    path('pneumonia/' , views.pneumoniaPage , name='vpneumonia'),
    path('heartDiseases/', views.heartDiseasesPage, name='vheartDiseases'),
]

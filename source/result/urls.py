from django.urls import path
from . import views

urlpatterns = [
    path('parkinsonsResult' , views.parkinsonsResult , name='parkinsonsResult'),
    path('diabetesResult' , views.diabetesResult , name='diabetesResult'),
    path('breastCancerResult' , views.breastCancerResult , name='breastCancerResult'),
    path('heartDiseasesResult', views.heartDiseasesResult, name='heartDiseasesResult'),
    path('pneumoniaResult', views.pneumoniaResult, name='pneumoniaResult'),
]

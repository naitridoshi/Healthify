from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('Quesitons', views.QuestionPage, name='questionPage'),
    path('recommended', views.RecommendedPage, name='recommendedPage'),
]

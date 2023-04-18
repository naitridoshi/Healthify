from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'temps/index.html')

def parkinsonsPage(request):
    return render(request , "diseases/parkinsons.html")


def breastCancerPage(request):
    return render(request , "diseases/breastCancer.html")


def diabetesPage(request):
    return render(request , "diseases/diabetes.html")

def heartDiseasesPage(request):
    return render(request , "diseases/heartDiseases.html")

def pneumoniaPage(request):
    return render(request , "diseases/pneumonia.html")
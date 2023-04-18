from django.shortcuts import render

# Create your views here.

def QuestionPage(request):
    return render(request , 'general/general.html')


def RecommendedPage(request):
    diabetes = 0
    breastCancer = 0
    parkinsons = 0
    heartDiseases = 0
    pneumonia = 0
    if request.method == 'POST':
        breastCancer = int(request.POST.get('breast_b1')) + int(request.POST.get('breast_b2')) + int(request.POST.get('breast_b3'))
        diabetes = int(request.POST.get(
            'diabetes_d1')) + int(request.POST.get('diabetes_d2')) + int(request.POST.get('diabetes_d3'))
        pneumonia = int(request.POST.get('pneumonia_pn1')) + int(
            request.POST.get('pneumonia_pn2')) + int(request.POST.get('pneumonia_pn3'))
        heartDiseases = int(request.POST.get(
            'heart_h1')) + int(request.POST.get('heart_h2')) + int(request.POST.get('heart_h3'))
        parkinsons = int(request.POST.get('parkinsons_p1')) + int(
            request.POST.get('parkinsons_p2')) + int(request.POST.get('parkinsons_p3'))
    return render(request, 'general/recommendedTest.html' , {'diabetes' : diabetes , 'breastCancer' : breastCancer , 'pneumonia' : pneumonia , 'heartdiseases' : heartDiseases , 'parkinsons' : parkinsons})


import PIL
import pickle
import pandas as pd
import numpy as np
from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
# from tf.keras.utils import image
import cv2
# Create your views here.
# Helper libraries
import numpy as np
import matplotlib.pyplot as pl

def parkinsonsResult(request):
    model = pickle.load(open('../ml_modules/model.parkinsons', 'rb'))
    mdvp_fo_hz = float(request.POST.get('mdvp_fo_hz'))
    mdvp_fhi_hz = float(request.POST.get('mdvp_fhi_hz'))
    mdvp_flo_hz = float(request.POST.get('mdvp_flo_hz'))
    mdvp_jitter_percent = float(request.POST.get('mdvp_jitter_percent'))
    mdvp_jitter_abs = float(request.POST.get('mdvp_jitter_abs'))
    mdvp_rap = float(request.POST.get('mdvp_rap'))
    mdvp_jitter_ppq = float(request.POST.get('mdvp_jitter_ppq'))
    jitter_ddp = float(request.POST.get('jitter_ddp'))
    mdvp_shimmer = float(request.POST.get('mdvp_shimmer'))
    mdvp_shimmer_db = float(request.POST.get('mdvp_shimmer_db'))
    shimmer_apq3 = float(request.POST.get('shimmer_apq3'))
    mdvp_shimmer_apq5 = float(request.POST.get('mdvp_shimmer_apq5'))
    mdvp_apq = float(request.POST.get('mdvp_apq'))
    shimmer_dda = float(request.POST.get('shimmer_dda'))
    nhr = float(request.POST.get('nhr'))
    hnr = float(request.POST.get('hnr'))
    rpde = float(request.POST.get('rpde'))
    d2 = float(request.POST.get('d2'))
    dfa = float(request.POST.get('dfa'))
    spread1 = float(request.POST.get('spread1'))
    spread2 = float(request.POST.get('spread2'))
    ppe = float(request.POST.get('ppe'))
    # ppe = float(ppe)
    # print(type(ppe))
    prop = []
    prop.extend([mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_percent, mdvp_jitter_abs, mdvp_rap, mdvp_jitter_ppq, jitter_ddp,
                 mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, mdvp_shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, rpde, d2, dfa, spread1, spread2, ppe])
    prop_data = pd.DataFrame(columns=['mdvp_fo_hz', 'mdvp_fhi_hz', 'mdvp_flo_hz', 'mdvp_jitter_percent', 'mdvp_jitter_abs', 'mdvp_rap', 'mdvp_jitter_ppq', 'jitter_ddp',
                                      'mdvp_shimmer', 'mdvp_shimmer_db', 'shimmer_apq3', 'mdvp_shimmer_apq5', 'mdvp_apq', 'shimmer_dda', 'nhr', 'hnr', 'rpde', 'd2', 'dfa', 'spread1', 'spread2', 'ppe'])
    prop_data.loc[len(prop)] = prop
    pred = model.predict(prop_data)
    result = type(ppe)
    if (pred == 1):
        result = "risk"
    else:
        result = "no risk"
    return render(request , 'result/parkinsonsResult.html' , {'result' : result})

def diabetesResult(request):
    model = pickle.load(open('../ml_modules/model.diabetes', 'rb'))
    result = 'shrut'
    if request.method == 'POST':
        age = (request.POST.get('age'))
        print(type(age))
        gender = request.POST.get('gender')
        # print(type(gender))
        # print(gender)
        polyuria = int(request.POST.get('polyuria'))
        # print(type(polyuria))
        # print(polyuria)
        polydipsia = int(request.POST.get('polydipsia'))
        sudden_weight_loss = int(request.POST.get('sudden_weight_loss'))
        weakness = int(request.POST.get('weakness'))
        polyphagia = int(request.POST.get('polyphagia'))
        genital_thrush = int(request.POST.get('genital_thrush'))
        visual_blurring = int(request.POST.get('visual_blurring'))
        itching = int(request.POST.get('itching'))
        irritatibility = int(request.POST.get('irritatibility'))
        delayed_healing = int(request.POST.get('delayed_healing'))
        partial_paresis = int(request.POST.get('partial_paresis'))
        muscle_stiffness = int(request.POST.get('muscle_stiffness'))
        alopecia = int(request.POST.get('alopecia'))
        obesity = int(request.POST.get('obesity'))

        prop = []
        prop.extend([age, polyuria, polydipsia, sudden_weight_loss, weakness, polyphagia, genital_thrush, visual_blurring,
                    itching, irritatibility, delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity])
        prop_data = pd.DataFrame(columns=['Age', 'Polyuria', 'Polydipsia', 'sudden weight loss',
                                            'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
                                            'Itching', 'Irritability', 'delayed healing', 'partial paresis',
                                            'muscle stiffness', 'Alopecia', 'Obesity'])
        prop_data.loc[len(prop)] = prop
        pred = model.predict(prop_data)
        if (pred == 1):
            result = "risk"
        else:
            result = "no risk"
    return render(request, 'result/diabetesResult.html', {'result': result})


def breastCancerResult(request):
    model = pickle.load(open('../ml_modules/model.breast_cancer', 'rb'))
    result = 'shrut'
    if request.method == 'POST':
        clump_thickness = int(request.POST.get('clump_thickness'))
        uniformity_of_cell_size = int(
            request.POST.get('uniformity_of_cell_size'))
        uniformity_of_cell_shape = int(
            request.POST.get('uniformity_of_cell_shape'))
        marginal_adhesion = int(request.POST.get('marginal_adhesion'))
        single_epithelial_cell_size = int(request.POST.get('single_epithelial_cell_size'))
        bare_nuclei = int(request.POST.get('bare_nuclei'))
        bland_chromatin = int(request.POST.get('bland_chromatin'))
        normal_nucleoli = int(request.POST.get('normal_nucleoli'))
        mitosis = int(request.POST.get('mitosis'))
        prop = []
        prop.extend([clump_thickness, uniformity_of_cell_size, uniformity_of_cell_shape, marginal_adhesion,
            single_epithelial_cell_size, bare_nuclei, bland_chromatin, normal_nucleoli, mitosis])
        prop_data = pd.DataFrame(columns=['Clump Thickness', 'Uniformity of Cell Size',
                                          'Uniformity of Cell Shape', 'Marginal Adhesion',
                                          'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                                          'Normal Nucleoli', 'Mitoses'])
        prop_data.loc[len(prop)] = prop
        pred = model.predict(prop_data)
        if (pred == 1):
            result = "risk"
        else:
            result = "no risk"
    return render(request, 'result/breastCancerResult.html', {'result' : result})

def heartDiseasesResult(request):
    result = 'shrut'
    if request.method == 'POST':
        model = pickle.load(open('../ml_modules/model.heart_disease_new', 'rb'))
        age=float(request.POST.get('age'))
        sex=(request.POST.get('sex'))
        chest_pain_type = float(request.POST.get('chest_pain_type'))
        resting_blood_pressure = float(
            request.POST.get('resting_blood_pressure'))
        serum_cholestrol = float(request.POST.get('serum_cholestrol'))
        fasting_blood_sugar = float(request.POST.get('fasting_blood_sugar'))
        resting_electrocardiographic_results = float(
            request.POST.get('resting_electrocardiographic_results'))
        maximum_heart_rate_achieved = float(
            request.POST.get('maximum_heart_rate_achieved'))
        exercise_induced_angina = float(
            request.POST.get('exercise_induced_angina'))
        oldpeak=float(request.POST.get('oldpeak'))
        slope_of_the_peak_exercise_ST_segment=float(request.POST.get('slope_of_the_peak_exercise_ST_segment'))
        # number_of_major_vessels_colored_by_flourosopy=float(request.POST.get('number_of_major_vessels_colored_by_flourosopy'))
        # thal= float(request.POST.get('thal'))                                                
        prop=[]
        prop.extend([age,chest_pain_type,resting_blood_pressure,serum_cholestrol,fasting_blood_sugar,fasting_blood_sugar,maximum_heart_rate_achieved,exercise_induced_angina,oldpeak,slope_of_the_peak_exercise_ST_segment])
        prop_data = pd.DataFrame(columns=['Age', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'])
        prop_data.loc[len(prop)] = prop
        pred = model.predict(prop_data)
        if(pred==1):
            result = 'risk'
        else:
            result = 'no risk'
    return render(request, 'result/heartDiseasesResult.html' , {'result' : result})


def pneumoniaResult(request):
    from PIL import Image
    # model = load_model("D:/Intellify/pneumonia_detection_ai_version_3.h5")
    model = load_model("../ml_modules/pneumonia_detection_ai_version_3.h5")
    # dimensions of our images
    img_width, img_height = 200, 200

    # load the model we saved
    # model = pickle.load(open('../ml_modules/model.pneumonia', 'rb'))
    result = 'shrut'    
    if request.method == 'POST':
        # creating a image object (main image)
        im1 = Image.open(request.FILES.get('image'))

        # save a image using extension
        im1 = im1.save("test.jpg")
        # path = request.FILES.get('image')
        path = './test.jpg'
        img = cv2.imread(path)
        img = cv2.resize(img, (200, 200))
        img = np.reshape(img, [-1, 200, 200, 1])
        img = np.array(img).reshape(-1, 200, 200, 1)
        img = img/255
        predictions = model.predict(img)
        # predicted_classes = np.argmax(predictions, axis=1)
        print(predictions)
        if(predictions[2] > predictions[0] ):
            result = 'risk'
        else:
            result = 'no risk'
    return render(request, 'result/pneumoniaResult.html' , {'result' : result})



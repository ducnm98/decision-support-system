from django.shortcuts import render, HttpResponse, loader, redirect
from datetime import datetime
from . import models, forms
from .dss.run import predictHF
import pandas as pd
from django_pandas.io import read_frame
import csv
import os
from django.db.models import Q

def index(request):
    context = {
        'today': datetime.now()
    }
    return render(request, 'homepage/index.html', context)

def patients(request):
    patients = models.patients.objects.all()
    context = {
        'patients': patients,
        'today': datetime.now()
    }
    return render(request, 'homepage/patients.html', context)

def patient_detail(request, id):
    patient = models.patients.objects.get(pk=id)
    context = {
        'patient': patient,
        'today': datetime.now()
    }
    return render(request, 'homepage/patients.html', context)

def patient_create(request):
    if request.method == 'POST':
        form = forms.patientsForm(request.POST)
        if form.is_valid():
            patients = models.patients.objects.all()
            # patientsA = models.patients.objects.exclude(ca=None).exclude(thal=None)
            # patientsB = models.patients.objects.filter(
            #     Q(ca__isnull=True) | Q(thal__isnull=True)
            # )
            
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            cp = form.cleaned_data['cp']
            trestbps = form.cleaned_data['trestbps']
            chol = form.cleaned_data['chol']
            fbs = form.cleaned_data['fbs']
            restecg = form.cleaned_data['restecg']
            thalach = form.cleaned_data['thalach']
            exang = form.cleaned_data['exang']
            oldpeak = form.cleaned_data['oldpeak']
            slope = form.cleaned_data['slope']
            ca = form.cleaned_data['ca']
            thal = form.cleaned_data['thal']
            df2 = pd.DataFrame([[
                name, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
            ]])
            
            predict = predictHF(patients, df2)
            predict = pd.DataFrame(predict)
            predict.columns = ['HF presence', 'HF absence']
            print('Predict', predict)
            # form.save()
            return render(request, 'homepage/result.html', { 'result': predict.to_html() })
        return render(request, 'homepage/partientsCreate.html', { 'form': form })
    return render(request, 'homepage/partientsCreate.html', { 'form': forms.patientsForm() })

def setup(request):
    models.patients.objects.all().delete()
    with open('Z:\Github\decision-support-system\projects\datawizard\processed_data.2.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'])
            name=row['name']
            if row['name'] == "None":
                name=None
            age=row['age']
            if row['age'] == "None":
                age=None
            sex=row['sex']
            if row['sex'] == "None":
                sex=None
            cp=row['cp']
            if row['cp'] == "None":
                cp=None
            trestbps=row['trestbps']
            if row['trestbps'] == "None":
                trestbps=None
            chol=row['chol']
            if row['chol'] == "None":
                chol=None
            fbs=row['fbs']
            if row['fbs'] == "None":
                fbs=None
            restecg=row['restecg']
            if row['restecg'] == "None":
                restecg=None
            thalach=row['thalach']
            if row['thalach'] == "None":
                thalach=None
            exang=row['exang']
            if row['exang'] == "None":
                exang=None
            oldpeak=row['oldpeak']
            if row['oldpeak'] == "None":
                oldpeak=None
            exang=row['exang']
            if row['exang'] == "None":
                exang=None
            slope=row['slope']
            if row['slope'] == "None":
                slope=None
            ca=row['ca']
            if row['ca'] == "None":
                ca=None
            thal=row['thal']
            if row['thal'] == "None":
                thal=None
            num=row['num']
            if row['num'] == "None":
                num=None
            p = models.patients(
                name=name,
                age=age,
                sex=sex,
                cp=cp,
                trestbps=trestbps,
                chol=chol,
                fbs=fbs,
                restecg=restecg,
                thalach=thalach,
                exang=exang,
                oldpeak=oldpeak,
                slope=slope,
                ca=ca,
                thal=thal,
                num=num,
            )
            # p = models.patients(
            #     name=row['name'],
            #     age=row['age'],
            #     sex=row['sex'],
            #     cp=row['cp'],
            #     trestbps=row['trestbps'],
            #     chol=row['chol'],
            #     fbs=row['fbs'],
            #     restecg=row['restecg'],
            #     thalach=row['thalach'],
            #     exang=row['exang'],
            #     oldpeak=row['oldpeak'],
            #     slope=row['slope'],
            #     ca=row['ca'],
            #     thal=row['thal'],
            #     num=row['num'],
            # )
            p.save()
    patients = models.patients.objects.all()
    context = {
        'patients': patients,
        'today': datetime.now()
    }
    return render(request, 'homepage/patients.html', context)
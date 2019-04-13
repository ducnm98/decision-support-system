from django.shortcuts import render, HttpResponse, loader, redirect
from datetime import datetime
from . import models, forms
from django.template.context_processors import csrf
from .dss.run import predictHF
import csv
import os

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

            # run(patients)
            predictHF(patients, form)
            form.save()
            return redirect('patients')
        return render(request, 'homepage/partientsCreate.html', { 'form': form })
    return render(request, 'homepage/partientsCreate.html', { 'form': forms.patientsForm() })

def setup(request):
    models.patients.objects.all().delete()
    with open('Z:\Github\decision-support-system\projects\datawizard\processed_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'])
            p = models.patients(
                name=row['name'],
                age=row['age'],
                sex=row['sex'],
                cp=row['cp'],
                trestbps=row['trestbps'],
                chol=row['chol'],
                fbs=row['fbs'],
                restecg=row['restecg'],
                thalach=row['thalach'],
                exang=row['exang'],
                oldpeak=row['oldpeak'],
                slope=row['slope'],
                ca=row['ca'],
                thal=row['thal'],
                num=row['num'],
            )
            p.save()
    patients = models.patients.objects.all()
    context = {
        'patients': patients,
        'today': datetime.now()
    }
    return render(request, 'homepage/patients.html', context)
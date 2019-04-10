from django.shortcuts import render, HttpResponse, loader, redirect
from datetime import datetime
from . import models, forms

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
            form.save()
            return redirect('patients')
        else:
            return render(request, 'homepage/partientsCreate.html', { 'form': form })
    else:
        return render(request, 'homepage/partientsCreate.html', { 'form': forms.patientsForm() })
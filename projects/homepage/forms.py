from django import forms
from . import models
class patientsForm(forms.ModelForm):
    class Meta:
        model = models.patients
        fields = ('name', 'ResultTest')

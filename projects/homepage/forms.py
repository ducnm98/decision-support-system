from django import forms
from . import models
class patientsForm(forms.ModelForm):
    class Meta:
        model = models.patients
        fields = ('name', 'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thai')

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('patients', views.patients),
    path('patients/create', views.patient_create, name="patient_create"),
    path('patients/<int:id>', views.patient_detail)
]
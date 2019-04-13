from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('setup', views.setup),
    path('patients', views.patients, name="patients"),
    path('patients/create', views.patient_create, name="patient_create"),
    path('patients/<int:id>', views.patient_detail, name="patient_detail")
]
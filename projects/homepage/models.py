from django.db import models

# Create your models here.   
class patients(models.Model):
    name = models.TextField()
    age = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    sex = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    cp = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    trestbps = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    chol = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    fbs = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    restecg = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    thalach = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    exang = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    oldpeak = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    slope = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    ca = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    thal = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    num = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name

class Weight(models.Model):
    age = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.DecimalField(max_digits=5, decimal_places=2)
    cp = models.DecimalField(max_digits=5, decimal_places=2)
    trestbps = models.DecimalField(max_digits=5, decimal_places=2)
    chol = models.DecimalField(max_digits=5, decimal_places=2)
    fbs = models.DecimalField(max_digits=5, decimal_places=2)
    restecg = models.DecimalField(max_digits=5, decimal_places=2)
    thalach = models.DecimalField(max_digits=5, decimal_places=2)
    exang = models.DecimalField(max_digits=5, decimal_places=2)
    oldpeak = models.DecimalField(max_digits=5, decimal_places=2)
    slope = models.DecimalField(max_digits=5, decimal_places=2)
    ca = models.DecimalField(max_digits=5, decimal_places=2)
    thai = models.DecimalField(max_digits=5, decimal_places=2)
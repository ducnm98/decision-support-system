import data_wizard
from . import models

data_wizard.register(models.patients)
data_wizard.register(models.ResultTest)
data_wizard.register(models.Weight)
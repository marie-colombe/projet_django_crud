from django.db import models

# Create your models here.

class Teachers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    date_birth = models.DateField()  
    matter = models.CharField(max_length=50)  
    phone = models.CharField(max_length=15)  
    city = models.CharField(max_length=50) 
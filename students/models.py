from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')], default='F')
    registration= models.CharField(max_length=15, unique=True, default='000000') 
    date_birth = models.DateField(default='2000-01-01')  
    level = models.CharField(max_length=50, default='Non spécifiée')  
    phone = models.CharField(max_length=15, default='0000000000')  
    city = models.CharField(max_length=50, default='Inconnue')  

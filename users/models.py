from django.db import models

# Create your models here.

class Users(models.Model):
   pseudo = models.CharField(max_length=10, unique=True)
   password = models.CharField(max_length=30)
   creat_at = models.DateField(auto_now_add=True)
    
   def __str__(self):
      return self.password

   class Meta:

      verbose_name = "user"
      verbose_name_plural = "user"
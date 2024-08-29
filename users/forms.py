from django import forms
from .models import Users

class UsersForm(forms.Form):
    pseudo = forms.CharField(label='Pseudo', max_length=10)
    password = forms.CharField(label='Password', max_length=50)
    creat_add = forms.DateField(label='Creat_add')
  
   
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields= ["pseudo","password",]
       # exclude = ("creat_at",)
        #fields="__all__" pour appeler tous les champs de notre modele
       

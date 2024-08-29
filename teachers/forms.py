from django import forms
from .models import Teachers

#class TeachersForm(forms.Form):
    #name = forms.CharField(label='Name', max_length=50)
    #last_name = forms.CharField(label='Last_name', max_length=50)
    #sex = forms.ChoiceField(label='Sex', choices=[('M', 'Masculin'), ('F', 'Féminin')])
    #date_birth = forms.DateField(label='Date_birth')
    #matter = forms.CharField(label='Matter', max_length=40)
    #phone = forms.CharField(label='Phone', max_length=15)
    #city = forms.CharField(label='City', max_length=25)


class TeachersForm(forms.ModelForm):

 class Meta:
        model = Teachers
        fields="__all__"





 
from django import forms
from django.contrib.auth.models import User


from .models import Maestro

class MaestroCreationForm(forms.ModelForm):
    
    class Meta:
        model = Maestro
        exclude = ['usuario']
        widgets = {
            'nacimiento':forms.DateInput(attrs={'type':'date'})
        }
    
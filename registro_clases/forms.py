from django import forms 

from .models import Clase

class ClaseCreateForm(forms.ModelForm):

    class Meta:
        model = Clase
        fields = [
            'asignatura',
            'fecha',
            'hora',
        ]
        widgets = {
            'fecha':forms.DateInput(attrs={'type':'date'}),
            'hora':forms.TimeInput(attrs={'type':'time'}),
        }
from django import forms 

from .models import Clase

class ClaseCreateForm(forms.ModelForm):

    class Meta:
        model = Clase
        fields = [
            'asignatura',
            'tipo',
            'fecha',
            'hora',
            'duracion',
        ]
        widgets = {
            'fecha':forms.DateInput(attrs={'type':'date'}),
            'hora':forms.TimeInput(attrs={'type':'time'}),
            'duracion':forms.NumberInput(attrs={'placeholder':'horas'})
        }
from django import forms
from .models import EvaluacionAmbiental

class EvaluacionAmbientalForm(forms.ModelForm):
    class Meta:
        model = EvaluacionAmbiental
        fields = '__all__'
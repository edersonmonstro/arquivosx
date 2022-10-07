from django import forms
from .models import CasosModel
 
 
# creating a form
class CasosForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = CasosModel
 
        # specify fields to be used
        fields = [
            "titulo",
            "tema",
        ]
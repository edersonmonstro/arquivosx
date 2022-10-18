from django import forms
from apps.cases.models import Case
 
 
# creating a form
class CasesForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Case
 
        # specify fields to be used
        fields = [
            "title",
            "theme",
        ]
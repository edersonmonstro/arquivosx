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

# class CasesForm(forms.ModelForm):
#     title = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'style': 'border-color: blue;',
#                 'placeholder': 'Case title here'
#             }
#         )
#     )
#     theme = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'style': 'border-color: blue;',
#                 'placeholder': 'Case theme here'
#             }
#         )
#     )
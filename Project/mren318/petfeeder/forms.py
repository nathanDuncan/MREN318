from django import forms
from petfeeder.models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['servingSize', 'servingTime1', 'servingTime2', 'name']
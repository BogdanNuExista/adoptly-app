from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class DogBreedForm(forms.Form):
    image = forms.ImageField(label="Upload a Dog Image")
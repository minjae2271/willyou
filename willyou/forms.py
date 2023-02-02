from django import forms
from .models import *

class CoupleForm(forms.ModelForm):
    class Meta:
        model = Couple
        fields = '__all__'

class WeddingImagesForm(forms.ModelForm):
    class Meta:
        model = WeddingImages
        fields = ('image',)
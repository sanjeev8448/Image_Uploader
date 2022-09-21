from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image_Upload
        fields = '__all__'
        labels = {'photo':''}
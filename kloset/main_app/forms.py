from django import forms
from .models import *

class ClothesForm(forms.ModelForm):

    class Meta:
        model = Clothes
        fields = ['name_of_item', 'brand', 'size', 'description', 'price', 'tags', 'availability', 'clothes_image']

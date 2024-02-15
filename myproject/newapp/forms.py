from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .models import Product
# creating a form


class AddHeroForm(forms.Form):
    name = forms.CharField(validators=[MaxLengthValidator(20), MinLengthValidator(2)])
    details = forms.CharField(max_length=500)
    img_url = forms.CharField(max_length=30)


# class AddHeroForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'details', 'img_url']



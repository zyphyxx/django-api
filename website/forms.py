from django import forms
from api.models import Category


class ProdForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    category = forms.ModelChoiceField(Category.objects.all())
    price = forms.DecimalField(max_digits=8)
    photo = forms.ImageField()




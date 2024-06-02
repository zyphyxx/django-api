from django import forms
from api.models import Category, Product


class ProdForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    category = forms.ModelChoiceField(Category.objects.all())
    price = forms.DecimalField(max_digits=8)
    photo = forms.ImageField()

    def save(self):
        product = Product(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            category=self.cleaned_data['category'],
            photo=self.cleaned_data['photo']
        )
        product.save()
        return product


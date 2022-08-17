from django import forms

from buyersapp.forms import BuyerRegistrationForm, BuyersProfileForm
from buyersapp.models import Buyer
from productsapp.models import Product
from productsapp.models import ProductCategory


class BuyerAdminRegistrationForm(BuyerRegistrationForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Buyer
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'age', 'password1', 'password2')


class BuyersAdminProfileForm(BuyersProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'readonly': False}))


class ProductAdminCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control form-select pt-3 pb-2', 'size': 1}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'image', 'category')


class ProductAdminChangeForm(ProductAdminCreateForm):
    pass

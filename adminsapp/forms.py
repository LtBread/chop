from django import forms

from buyersapp.forms import BuyerRegistrationForm, BuyersProfileForm
from buyersapp.models import Buyer
from productsapp.models import Product


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


class ProductAdminCreate(forms.ModelForm):
    pass
    # class Meta:
    #     model = Product
    #     fields = ('name ',)

from django import forms

from buyersapp.forms import BuyerRegistrationForm
from buyersapp.models import Buyer


class BuyerAdminRegistrationForm(BuyerRegistrationForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Buyer
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'age', 'password1', 'password2')

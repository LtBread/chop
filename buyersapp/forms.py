from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from buyersapp.models import Buyer


class BuyerLoginForm(AuthenticationForm):
    # def __init__(self, *args, **kwargs):
    #     super(BuyerLoginForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = Buyer
        fields = ('username', 'password')


class BuyerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите возраст'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Buyer
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            print('Регистрация позволена пользователям от 18 лет')
            raise forms.ValidationError('Регистрация позволена пользователям от 18 лет')
        return data

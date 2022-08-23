from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator

from buyersapp.models import Buyer
from basketsapp.models import Basket
from productsapp.models import Product
from buyersapp.forms import BuyerLoginForm, BuyerRegistrationForm, BuyersProfileForm


class BuyerLoginView(LoginView):
    model = Buyer
    form_class = BuyerLoginForm
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Chop - Авторизация'}
    template_name = 'buyersapp/login.html'

# def login(request):
#     if request.method == 'POST':
#         form = BuyerLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = BuyerLoginForm()
#
#     context = {'title': 'Chop - Авторизация', 'form': form}
#     return render(request, 'buyersapp/login.html', context)


# class RegistrationView(View):
#     def get(self, request, *args, **kwargs):
#         form = BuyerRegistrationForm()
#         context = {
#             'title': 'Chop - Регистрация',
#             'form': form
#         }
#         return render(request, 'buyersapp/registration.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = BuyerRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('buyers:login'))


def registration(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('buyers:login'))
    else:
        form = BuyerRegistrationForm()

    context = {'title': 'Chop - Регистрация', 'form': form}
    return render(request, 'buyersapp/registration.html', context)


# class ProfileView(UpdateView):
#     model = Buyer
#     form_class = BuyersProfileForm
#     success_url = reverse_lazy('buyers:profile')
#     template_name = 'buyersapp/profile.html'
#
#     def get(self):
#         pass
#
#     @method_decorator(login_required)
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)


@login_required
def profile(request):
    user = request.user
    baskets = Basket.objects.filter(buyer=user)
    # product = Product.objects.get(id=baskets.product)
    if request.method == 'POST':
        form = BuyersProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно изменены!')
            return HttpResponseRedirect(reverse('buyers:profile'))
    else:
        form = BuyersProfileForm(instance=user)

    context = {
        'title': 'Chop - Личный кабинет',
        'form': form,
        'baskets': baskets,
        # 'product': product
    }
    return render(request, 'buyersapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

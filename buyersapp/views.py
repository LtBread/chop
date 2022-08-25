from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView

from buyersapp.models import Buyer
from basketsapp.models import Basket
from buyersapp.forms import BuyerLoginForm, BuyerRegistrationForm, BuyersProfileForm


class BuyerLoginView(LoginView):
    model = Buyer
    form_class = BuyerLoginForm
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Chop - Авторизация'}
    template_name = 'buyersapp/login.html'


class BuyerRegistrationView(CreateView):
    model = Buyer
    form_class = BuyerRegistrationForm
    success_url = reverse_lazy('buyers:login')
    extra_context = {'title': 'Chop - Регистрация'}
    template_name = 'buyersapp/registration.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Вы успешно зарегистрировались!')
        return super().post(request, *args, **kwargs)


class BuyerProfileView(UpdateView):
    model = Buyer
    form_class = BuyersProfileForm
    template_name = 'buyersapp/profile.html'

    def get_success_url(self):
        return reverse_lazy('buyers:profile', args=(self.object.id,))

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Данные успешно изменены!')
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BuyerProfileView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Личный кабинет'
        context['baskets'] = Basket.objects.filter(buyer=self.object.id)
        return context


class BuyerLogoutView(LogoutView):
    pass

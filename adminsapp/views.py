from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models.deletion import ProtectedError
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from buyersapp.models import Buyer
from productsapp.models import Product, ProductCategory
from adminsapp.forms import AdminBuyerRegistrationForm, AdminBuyersProfileForm, AdminProductCreateForm, \
    AdminProductChangeForm, AdminCategoryCreateForm, AdminCategoryChangeForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Chop - Админ-панель'}
    return render(request, 'adminsapp/index.html', context)


""" BUYERS """


class AdminBuyerListView(ListView):
    model = Buyer
    template_name = 'adminsapp/buyers/admin-buyers.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminBuyerListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminBuyerListView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Покупатели'
        return context


class AdminBuyerCreateView(CreateView):
    model = Buyer
    form_class = AdminBuyerRegistrationForm
    success_url = reverse_lazy('admins:buyers')
    template_name = 'adminsapp/buyers/admin-buyer-create.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminBuyerCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminBuyerCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Создание покупателей'
        return context


class AdminBuyerUpdateView(UpdateView):
    model = Buyer
    form_class = AdminBuyersProfileForm
    success_url = reverse_lazy('admins:buyers')
    template_name = 'adminsapp/buyers/admin-buyer-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminBuyerUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminBuyerUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Редактирование покупателей'
        return context


class AdminBuyerChangeActivityView(DeleteView):
    model = Buyer
    success_url = reverse_lazy('admins:buyers')
    template_name = 'adminsapp/buyers/admin-buyer-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminBuyerChangeActivityView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.change_activity()
        return HttpResponseRedirect(success_url)


""" PRODUCTS """


class AdminProductListView(ListView):
    model = Product
    template_name = 'adminsapp/products/admin-products.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Товары'
        return context


class AdminProductCreateView(CreateView):
    model = Product
    form_class = AdminProductCreateForm
    success_url = reverse_lazy('admins:products')
    template_name = 'adminsapp/products/admin-product-create.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Создание товаров'
        return context


class AdminProductUpdateView(UpdateView):
    model = Product
    form_class = AdminProductChangeForm
    success_url = reverse_lazy('admins:products')
    template_name = 'adminsapp/products/admin-product-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Редактирование товаров'
        return context


class AdminProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('admins:products')
    template_name = 'adminsapp/products/admin-product-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductDeleteView, self).dispatch(request, *args, **kwargs)


""" CATEGORY """


class AdminCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminsapp/categories/admin-categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCategoryListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - Категории товаров'
        return context


class AdminCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = AdminCategoryCreateForm
    success_url = reverse_lazy('admins:categories')
    template_name = 'adminsapp/categories/admin-category-create.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCategoryCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - создание категорий товаров'
        return context


class AdminCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = AdminCategoryChangeForm
    success_url = reverse_lazy('admins:categories')
    template_name = 'adminsapp/categories/admin-category-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCategoryUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Chop - редактирование статьи'
        return context


class AdminCategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admins:categories')
    template_name = 'adminsapp/categories/admin-category-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCategoryDeleteView, self).dispatch(request, *args, **kwargs)


""" Buyer LIST """
# @user_passes_test(lambda u: u.is_superuser)
# def admin_buyers(request):
#     context = {
#         'title': 'Chop - Покупатели',
#         'buyers': Buyer.objects.all()
#     }
#     return render(request, 'adminsapp/buyers/admin-buyers.html', context)


""" Buyer CREATE """
# @user_passes_test(lambda u: u.is_superuser)
# def admin_buyer_create(request):
#     if request.method == 'POST':
#         form = AdminBuyerRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь создан!')
#             return HttpResponseRedirect(reverse('admins:buyers'))
#     else:
#         form = AdminBuyerRegistrationForm()
#     context = {
#         'title': 'Chop - Создание покупателей',
#         'form': form
#     }
#     return render(request, 'adminsapp/buyers/admin-buyer-create.html', context)


""" Buyer UPDATE """
# @user_passes_test(lambda u: u.is_superuser)
# def admin_buyer_update(request, buyer_id):
#     selected_buyer = Buyer.objects.get(id=buyer_id)
#     if request.method == 'POST':
#         form = AdminBuyersProfileForm(instance=selected_buyer, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Данные пользователя успешно изменены!')
#             return HttpResponseRedirect(reverse('admins:buyers'))
#     else:
#         form = AdminBuyersProfileForm(instance=selected_buyer)
#     context = {
#         'title': 'Chop - Редактирование покупателей',
#         'form': form,
#         'selected_buyer': selected_buyer
#     }
#     return render(request, 'adminsapp/buyers/admin-buyer-update-delete.html', context)


""" Buyer DELETE """
# @user_passes_test(lambda u: u.is_superuser)
# def admin_buyer_change_activity(request, buyer_id):
#     buyer = Buyer.objects.get(id=buyer_id)
#     buyer.change_activity()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])


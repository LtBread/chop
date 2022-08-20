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


# @user_passes_test(lambda u: u.is_superuser)
# def admin_buyers(request):
#     context = {
#         'title': 'Chop - Покупатели',
#         'buyers': Buyer.objects.all()
#     }
#     return render(request, 'adminsapp/buyers/admin-buyers.html', context)


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


class AdminBuyerChangeActivityView(DeleteView):
    model = Buyer
    success_url = reverse_lazy('admins:buyers')
    template_name = 'adminsapp/buyers/admin-buyer-update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminBuyerChangeActivityView, self).dispatch(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.change_activity()
    #     return HttpResponseRedirect(success_url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.change_activity()
        return HttpResponseRedirect(success_url)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_buyer_change_activity(request, buyer_id):
#     buyer = Buyer.objects.get(id=buyer_id)
#     buyer.change_activity()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    context = {
        'title': 'Chop - Товары',
        'products': Product.objects.all()
    }
    return render(request, 'adminsapp/products/admin-products.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_create(request):
    if request.method == 'POST':
        form = AdminProductCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар создан!')
            return HttpResponseRedirect(reverse('admins:products'))
    else:
        form = AdminProductCreateForm()
    context = {
        'title': 'Chop - Создание товаров',
        'form': form
    }
    return render(request, 'adminsapp/products/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_update(request, product_id):
    selected_product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = AdminProductChangeForm(instance=selected_product, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные товара успешно изменены!')
            return HttpResponseRedirect(reverse('admins:products'))
    else:
        form = AdminProductChangeForm(instance=selected_product)
    context = {
        'title': 'Chop - Редактирование товаров',
        'form': form,
        'selected_product': selected_product
    }
    return render(request, 'adminsapp/products/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_change_activity(request, product_id):
    product = Product.objects.get(id=product_id)
    product.change_activity()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@user_passes_test(lambda u: u.is_staff)
def admin_categories(request):
    categories = ProductCategory.objects.all()
    context = {
        'title': 'Chop - Категории товаров',
        'categories': categories
    }
    return render(request, 'adminsapp/categories/admin-categories.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_create(request):
    if request.method == 'POST':
        form = AdminCategoryCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория товаров создана!')
            return HttpResponseRedirect(reverse('admins:categories'))
    else:
        form = AdminCategoryCreateForm()
    context = {
        'title': 'Chop - Создание категорий товаров',
        'form': form
    }
    return render(request, 'adminsapp/categories/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_update(request, category_id):
    selected_category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = AdminCategoryChangeForm(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные категории успешно изменены!')
            return HttpResponseRedirect(reverse('admins:categories'))
    else:
        form = AdminCategoryChangeForm(instance=selected_category)
    context = {
        'title': 'Chop - Редактирование категорий',
        'form': form,
        'selected_category': selected_category
    }
    return render(request, 'adminsapp/categories/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_delete(request, category_id):
    try:
        category = ProductCategory.objects.get(id=category_id)
        category.delete()
        messages.success(request, 'Категория успешно удалена!')
    except ProtectedError:
        messages.warning(request, 'Ошибка удаления категории: существуют товары данной категории! '
                                  'Для удаления категории переведите товары в другую категорию.')
    return HttpResponseRedirect(reverse('admins:categories'))

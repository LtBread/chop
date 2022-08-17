"""chop URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from productsapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('productsapp.urls', namespace='products')),
    path('buyers/', include('buyersapp.urls', namespace='buyers')),
    path('baskets/', include('basketsapp.urls', namespace='baskets')),
    path('admins/', include('adminsapp.urls', namespace='admins')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

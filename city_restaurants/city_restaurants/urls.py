from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include('restaurants.urls')),
    path('', lambda request: redirect('restaurant_list')),  # Редирект на список ресторанов
]

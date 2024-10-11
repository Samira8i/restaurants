from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_restaurant, name='add_restaurant'),
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/delete/', views.delete_restaurant, name='delete_restaurant'),
    path('<int:restaurant_id>/edit/', views.edit_restaurant, name='edit_restaurant'),
    path('search/', views.search_restaurant, name='search_restaurant'),  # Маршрут для поиска
]

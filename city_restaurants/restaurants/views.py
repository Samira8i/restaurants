from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from .forms import RestaurantForm

# Добавление ресторана
def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/add_restaurant.html', {'form': form})

# Отображение всех ресторанов
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

# Удаление ресторана
def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'restaurants/delete_restaurant.html', {'restaurant': restaurant})

# Изменение ресторана
def edit_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurants/edit_restaurant.html', {'form': form})

# Поиск по специализации
def search_restaurant(request):
    query = request.GET.get('q')
    restaurants = Restaurant.objects.filter(specialization__icontains=query)
    return render(request, 'restaurants/search_results.html', {'restaurants': restaurants, 'query': query})

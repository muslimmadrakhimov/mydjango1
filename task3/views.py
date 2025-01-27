from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'third_task/index.html')

# Страница Магазин
def shop(request):
    items = {
        'item1': 'Игровая приставка',
        'item2': 'Игровая мышь',
        'item3': 'Игровой монитор',
    }
    return render(request, 'third_task/shop.html', {'items': items})

# Страница Корзина
def cart(request):
    return render(request, 'third_task/cart.html')


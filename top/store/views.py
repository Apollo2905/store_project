from django.shortcuts import render, redirect
from .models import Product, SliderImage


def home(request):
    products = Product.objects.all()
    slides = SliderImage.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    # отловить значение атрибута product
    # *** делать проверку на наличие такого продукта в корзине,
    # если такой продукт был ранее добавлен, то нужно
    # всего лишь поле quantity на 1, если нет, то создать CartItem

    products = products.filter(category=category) if category else products
    products = products.filter(brand=brand) if brand else products

    return render(request, 'home.html', {'products': products, 'slides': slides})


# реализовать показ добавленных в корзину продуктов (м-в-ш, MTV)

# добавить кнопку в навбаре для перехода в корзину

#в шаблонизаторе добавьте кнопку "назад"
#а продукты корзины показать в виде таблицы
#имя продукта, цена продукта, количество(quantity), сумму общая
from django.shortcuts import render, redirect
from .models import Product, SliderImage, Guest, CartItem
from django.http import HttpResponse


def home(request):
    products = Product.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    slides = SliderImage.objects.all()

    products = products.filter(category=category) if category else products
    products = products.filter(brand=brand) if brand else products

    return render(request, 'home.html', {'products': products, 'slides': slides})


def product(request, pk):
    product_data = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product': product_data})


def guest_register(request, pk):
    token = request.COOKIES['csrftoken']
    guest = Guest.objects.filter(token=token)

    if not guest:
        Guest.objects.create(token=token)

    cart_item = CartItem.objects.filter()


    return redirect('store:home')


def cart(request):
    return render(request, 'cart.html', {})

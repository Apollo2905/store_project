from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    category = request.GET.get('category')
    products = products.filter(category=category) if category else products
    return render(request, 'home.html', {'products': products})



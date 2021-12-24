from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def categories(request):
    categories = Category.objects.all()

    return {'categories': categories}


def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'store/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)

    context = {
        'products': product,
    }
    return render(request, 'store/products/detail.html', context)


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store/products/category.html', context)

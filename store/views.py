from carts.models import CartItem
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category
from carts.views import _cart_id


def store(request,category_slug=None):
    categories = None,
    products = None,
    
    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context ={
        'products':products,
        'product_count':product_count,

    }
    return render(request,'store/store.html',context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter( product=single_product).exists()  #i just remove this cart__cart_id = _cart_id(request),
    
    except Exception as e:
        raise
    context = {
            'single_product':single_product,
            'in_cart': in_cart
    }
    return render(request, 'store/product_detail.html', context)

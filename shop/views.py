from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def index(request):
    featured_product = Product.objects.filter(featureproduct=True).first()
    recently_updated_books = Product.objects.filter().order_by('-updated')[:3]
    context = {'featured_product': featured_product,'recently_updated_books': recently_updated_books}
    return render(request, 'shop/product/home.html', context )

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    featured_product = Product.objects.filter(featureproduct=True).first()
    if category_slug:
        category = get_object_or_404(Category,slug = category_slug)
        products = products.filter(category=category)
    context = {'category':category,'categories':categories,'products':products,'featured_product': featured_product}
    return render(request, 'shop/product/books.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'shop/product/bookdetail.html', context)
    



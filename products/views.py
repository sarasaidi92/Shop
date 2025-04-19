from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

def products(request):
    listings = Product.objects.order_by('-product_date')
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
    }
    return render(request, 'products.html', context=context)

def single_product(request):

    return render(request, 'single_product.html')
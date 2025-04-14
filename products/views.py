from django.shortcuts import render

def products(request):
    return render(request, 'products.html')

def single_product(request):
    return render(request, 'single_product.html')
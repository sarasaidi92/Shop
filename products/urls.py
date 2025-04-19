from django.urls import path
from .views import products, single_product


urlpatterns = [
    path('', products, name='products'),
    path('single/', single_product, name='single_product'),

]
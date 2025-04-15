from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

class Product(models.Model):
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    text = RichTextField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    score = RichTextField(blank=True)
    price = models.FloatField(default=0)
    description = RichTextField(blank=True)
    number_of_orders = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    is_published = models.BooleanField(default=True)
    product_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


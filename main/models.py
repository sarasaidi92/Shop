from idlelib.mainmenu import menudefs
from random import choices

from django.db import models
from ckeditor.fields import RichTextField

class Basic(models.Model):
    title = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    men = 'men'
    women = 'women'
    kids = 'kids'

    shop_choices = (
        (men, 'men'),
        (women, 'women'),
        (kids, 'kids'),
    )

    category = models.CharField(max_length=100, choices= shop_choices , blank=True)
    useful_links = models.CharField(max_length=100, blank=True)
    information = models.CharField(max_length=100, blank=True)

    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    behance = models.TextField(blank=True)

    footer = RichTextField(blank=True)



    def __str__(self):
        return self.title



from idlelib.mainmenu import menudefs
from random import choices

from django.db import models
from ckeditor.fields import RichTextField

class Basic(models.Model):
    title = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    title_shopping = models.CharField(max_length=50, blank=True)
    men = models.CharField(max_length=50, blank=True)
    women = models.CharField(max_length=50, blank=True)
    kids = models.CharField(max_length=50, blank=True)

    useful_links = models.CharField(max_length=50, blank=True)
    homepage = models.CharField(max_length=50, blank=True)
    about = models.CharField(max_length=50, blank=True)
    help = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=50, blank=True)

    information = models.CharField(max_length=50, blank=True)
    help_info = models.CharField(max_length=50, blank=True)
    faq = models.CharField(max_length=50, blank=True)
    shipping = models.CharField(max_length=50, blank=True)
    tracking = models.CharField(max_length=50, blank=True)


    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    behance = models.TextField(blank=True)

    footer = RichTextField(blank=True)



    def __str__(self):
        return self.title



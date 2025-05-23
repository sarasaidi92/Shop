# Generated by Django 5.2 on 2025-04-15 06:59

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('score', ckeditor.fields.RichTextField()),
                ('price', models.FloatField(default=0)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('number_of_orders', models.IntegerField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('image_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('image_detail', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('product_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]

# Generated by Django 5.2 on 2025-04-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic',
            name='category',
            field=models.CharField(blank=True, choices=[('men', 'men'), ('women', 'women'), ('kids', 'kids')], max_length=100),
        ),
    ]

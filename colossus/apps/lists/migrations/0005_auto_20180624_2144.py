# Generated by Django 2.0.6 on 2018-06-24 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20180619_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='list short URL'),
        ),
    ]
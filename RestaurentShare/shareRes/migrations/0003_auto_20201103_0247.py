# Generated by Django 2.2.1 on 2020-11-02 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareRes', '0002_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurent_content',
            new_name='restaurant_content',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurent_keyword',
            new_name='restaurant_keyword',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurent_link',
            new_name='restaurant_link',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurent_name',
            new_name='restaurant_name',
        ),
    ]

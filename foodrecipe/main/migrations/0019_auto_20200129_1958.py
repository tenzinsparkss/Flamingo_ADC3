# Generated by Django 3.0.1 on 2020-01-29 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='item',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]

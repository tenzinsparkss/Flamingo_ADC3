# Generated by Django 3.0.2 on 2020-02-02 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200201_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_image',
        ),
    ]

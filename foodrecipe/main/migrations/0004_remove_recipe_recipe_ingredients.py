# Generated by Django 3.0.1 on 2020-01-25 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200122_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_ingredients',
        ),
    ]
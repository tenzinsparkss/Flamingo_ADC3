# Generated by Django 3.0.1 on 2020-01-29 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200129_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='flag',
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-04 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedback_submit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='submit',
            new_name='subject',
        ),
    ]
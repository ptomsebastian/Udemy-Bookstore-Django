# Generated by Django 3.2.20 on 2023-08-19 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_auto_20230819_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
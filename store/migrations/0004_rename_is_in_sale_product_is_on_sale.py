# Generated by Django 4.2.11 on 2024-06-12 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_is_insale_product_is_in_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_in_sale',
            new_name='is_on_sale',
        ),
    ]

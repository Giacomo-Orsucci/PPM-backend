# Generated by Django 4.2.11 on 2024-06-12 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product_is_insale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_inSale',
            new_name='is_in_sale',
        ),
    ]

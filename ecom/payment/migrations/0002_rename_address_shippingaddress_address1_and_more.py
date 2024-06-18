# Generated by Django 4.2.11 on 2024-06-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

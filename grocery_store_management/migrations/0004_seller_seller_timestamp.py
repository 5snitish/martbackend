# Generated by Django 3.0.6 on 2021-01-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store_management', '0003_auto_20210122_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='Seller_Timestamp',
            field=models.DateField(auto_now=True),
        ),
    ]

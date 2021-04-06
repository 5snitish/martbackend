# Generated by Django 3.0.6 on 2021-01-22 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchased_product',
            name='order',
        ),
        migrations.AddField(
            model_name='purchased_product',
            name='seller_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grocery_store_management.Seller'),
            preserve_default=False,
        ),
    ]

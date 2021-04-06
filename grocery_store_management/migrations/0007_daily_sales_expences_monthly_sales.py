# Generated by Django 3.0.6 on 2021-01-28 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store_management', '0006_auto_20210127_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_name', models.CharField(max_length=40)),
                ('exp_disc', models.CharField(max_length=100)),
                ('exp_amaount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_sales', models.DecimalField(decimal_places=2, max_digits=30)),
                ('daily_sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery_store_management.Daily_sales')),
            ],
        ),
    ]

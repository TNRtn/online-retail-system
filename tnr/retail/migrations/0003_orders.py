# Generated by Django 3.0 on 2023-11-21 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0002_auto_20231121_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('orderid', models.IntegerField(primary_key=True, serialize=False)),
                ('orderdate', models.DateField(null=True)),
                ('shippingaddress', models.CharField(max_length=255)),
                ('paymentmethod', models.CharField(max_length=255)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.customer')),
            ],
        ),
    ]
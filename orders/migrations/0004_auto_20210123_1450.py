# Generated by Django 3.1.3 on 2021-01-23 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authln', '0003_auto_20210121_1400'),
        ('orders', '0003_shoppinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shoping_customer', to='authln.custumer'),
        ),
    ]

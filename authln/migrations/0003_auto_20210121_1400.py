# Generated by Django 3.1.3 on 2021-01-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authln', '0002_custumer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='custumer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]

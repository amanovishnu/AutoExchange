# Generated by Django 3.2.18 on 2023-03-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20230310_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(default=135606),
        ),
    ]

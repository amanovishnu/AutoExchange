# Generated by Django 3.2.18 on 2023-03-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20230312_2142'),
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
            field=models.IntegerField(default=149888),
        ),
    ]

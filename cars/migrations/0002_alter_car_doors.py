# Generated by Django 3.2.18 on 2023-03-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6']], default='1'),
        ),
    ]
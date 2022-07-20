# Generated by Django 3.2.8 on 2022-07-20 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0003_auto_20220717_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date_from',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 20, 13, 19, 16, 240192), null=True, verbose_name='Прибытие'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_to',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 20, 13, 19, 16, 240216), null=True, verbose_name='Выезд'),
        ),
    ]

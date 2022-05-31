# Generated by Django 3.0.3 on 2021-09-16 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ListOfCountries",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=64, unique=True, verbose_name="имя"),
                ),
                ("description", models.TextField(blank=True, verbose_name="описание")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активна"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Regions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=64, unique=True, verbose_name="имя"),
                ),
                ("description", models.TextField(blank=True, verbose_name="описание")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активна"),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.ListOfCountries",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accommodation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="название проживания"
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="accommodation_img")),
                (
                    "short_desc",
                    models.TextField(
                        blank=True,
                        max_length=60,
                        verbose_name="краткое описание продукта",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="описание продукта"),
                ),
                (
                    "availability",
                    models.PositiveIntegerField(
                        verbose_name="количество свободных номеров"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="цена"
                    ),
                ),
                (
                    "room_desc",
                    models.TextField(
                        blank=True,
                        max_length=60,
                        verbose_name="краткое описание комнаты",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активна"),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.ListOfCountries",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.Regions",
                    ),
                ),
            ],
        ),
    ]

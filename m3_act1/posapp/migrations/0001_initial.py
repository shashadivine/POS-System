# Generated by Django 4.2.11 on 2024-04-16 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=300)),
                ("item_price", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cafe",
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
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("Café Expresso", "Café Expresso"),
                            ("Café com Leite", "Café com Leite"),
                            ("Cappuccino", "Cappuccino"),
                            ("Mocha", "Mocha"),
                            ("Latte", "Latte"),
                        ],
                        max_length=50,
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("ingredientes", models.TextField()),
                ("tamanho_copo", models.PositiveIntegerField()),
                ("valor", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
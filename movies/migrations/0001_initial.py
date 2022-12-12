# Generated by Django 4.1.3 on 2022-12-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(default=None, max_length=10, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "G"),
                            ("PG", "Pg"),
                            ("PG-13", "Pgthirteen"),
                            ("R", "R"),
                            ("NC-17", "Nc"),
                        ],
                        default="G",
                        max_length=20,
                        null=True,
                    ),
                ),
                ("synopsisPetSex", models.TextField(default=None, null=True)),
            ],
        ),
    ]
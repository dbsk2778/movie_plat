# Generated by Django 4.1.3 on 2023-03-08 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StayTime",
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
                ("title", models.CharField(max_length=100)),
                ("second", models.IntegerField()),
            ],
        ),
    ]

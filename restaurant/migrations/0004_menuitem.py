# Generated by Django 4.1.4 on 2023-12-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "restaurant",
            "0003_remove_booking_comment_remove_booking_guest_number_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuItem",
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
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("inventory", models.SmallIntegerField()),
            ],
        ),
    ]

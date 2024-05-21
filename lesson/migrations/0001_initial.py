# Generated by Django 5.0.4 on 2024-04-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("lname", models.CharField(max_length=100)),
                ("jianjie", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "实验课程",
                "verbose_name_plural": "实验课程",
            },
        ),
    ]
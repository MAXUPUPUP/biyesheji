# Generated by Django 5.0.4 on 2024-04-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shiyan", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shiyan",
            name="file",
            field=models.FileField(default=1, upload_to="shiyan"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shiyan",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]

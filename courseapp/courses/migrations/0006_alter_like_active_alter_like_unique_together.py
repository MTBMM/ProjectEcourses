# Generated by Django 4.2.6 on 2024-03-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0005_rating_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("user", "lesson")},
        ),
    ]

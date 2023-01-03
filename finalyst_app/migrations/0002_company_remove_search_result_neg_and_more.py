# Generated by Django 4.1.4 on 2022-12-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finalyst_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("title", models.TextField(blank=True, default="", null=True)),
                ("pos1", models.TextField(blank=True, default="", null=True)),
                ("pos2", models.TextField(blank=True, default="", null=True)),
                ("pos3", models.TextField(blank=True, default="", null=True)),
                ("pos4", models.TextField(blank=True, default="", null=True)),
                ("pos5", models.TextField(blank=True, default="", null=True)),
                ("neg1", models.TextField(blank=True, default="", null=True)),
                ("neg2", models.TextField(blank=True, default="", null=True)),
                ("neg3", models.TextField(blank=True, default="", null=True)),
                ("neg4", models.TextField(blank=True, default="", null=True)),
                ("neg5", models.TextField(blank=True, default="", null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="search",
            name="result_neg",
        ),
        migrations.RemoveField(
            model_name="search",
            name="result_pos",
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-19 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_task"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-date_created"]},
        ),
    ]

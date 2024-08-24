# Generated by Django 5.1 on 2024-08-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0025_alter_repository_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="repository",
            name="commits_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Commits count"),
        ),
    ]

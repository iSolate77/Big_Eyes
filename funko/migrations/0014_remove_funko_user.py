# Generated by Django 4.1.4 on 2023-01-11 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("funko", "0013_funko_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="funko",
            name="user",
        ),
    ]
# Generated by Django 4.1.4 on 2023-01-09 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("funko", "0005_address_orderfunko_delete_orderdetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="country",
            field=django_countries.fields.CountryField(default="1", max_length=2),
        ),
        migrations.AlterField(
            model_name="address",
            name="user",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
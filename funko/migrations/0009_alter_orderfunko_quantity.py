# Generated by Django 4.1.4 on 2023-01-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko', '0008_alter_order_address_alter_order_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfunko',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
# Generated by Django 4.1.4 on 2023-01-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko', '0010_order_is_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

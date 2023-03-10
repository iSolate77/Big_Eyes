# Generated by Django 4.1.4 on 2023-01-10 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funko', '0006_address_country_alter_address_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funko',
            name='item_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='orderfunko',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='funko.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='funko.orderfunko'),
        ),
        migrations.AddField(
            model_name='orderfunko',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderfunko',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderfunko',
            name='funko',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='funko.funko'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]

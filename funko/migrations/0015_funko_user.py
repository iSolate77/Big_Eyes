# Generated by Django 4.1.4 on 2023-01-11 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funko', '0014_remove_funko_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='funko',
            name='user',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
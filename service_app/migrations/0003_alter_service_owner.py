# Generated by Django 3.2.25 on 2025-05-02 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0002_service_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

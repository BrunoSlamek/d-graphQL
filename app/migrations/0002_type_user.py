# Generated by Django 4.2.2 on 2023-09-30 14:31

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.3 on 2021-07-19 10:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='allowed_user',
            field=models.ManyToManyField(blank=True, related_name='allowed_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
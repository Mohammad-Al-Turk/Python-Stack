# Generated by Django 5.1.3 on 2024-11-22 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
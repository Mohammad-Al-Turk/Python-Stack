# Generated by Django 2.2.4 on 2024-11-04 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='commentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commented_messages', to='users_app.User'),
        ),
    ]

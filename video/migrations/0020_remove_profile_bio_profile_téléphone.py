# Generated by Django 4.0.3 on 2022-09-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0019_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='Téléphone',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]

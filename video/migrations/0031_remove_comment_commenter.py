# Generated by Django 4.0.3 on 2022-10-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0030_comment_commenter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
    ]

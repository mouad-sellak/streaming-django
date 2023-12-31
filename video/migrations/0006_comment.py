# Generated by Django 4.0.3 on 2022-09-13 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_favorite_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('documentaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.documentaire')),
                ('episode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.episode')),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.film')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='video.music')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-09-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0021_alter_profile_téléphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ville',
            field=models.CharField(choices=[('Nouakchott ', 'Nouakchott '), ('Trarza  ', 'Trarza  '), ('Hodh_Chargui', 'Hodh_Chargui'), ('Gorgol ', 'Gorgol '), ('Assaba ', 'Assaba '), ('Brakna  ', 'Brakna  '), ('Hodh_Gharbi  ', 'Hodh_Gharbi '), ('Guidimaka  ', 'Guidimaka  '), ('Nouadhibou ', 'Nouadhibou '), ('Adrar ', 'Adrar '), ('Zouérate', 'Zouérate'), ('Inchiri ', 'Inchiri ')], default='serie', max_length=100, null=True),
        ),
    ]
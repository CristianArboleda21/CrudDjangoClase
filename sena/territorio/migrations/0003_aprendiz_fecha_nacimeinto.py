# Generated by Django 4.0.6 on 2022-07-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0002_rename_actividadrealizada_actividades_actividad_realizada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aprendiz',
            name='fecha_nacimeinto',
            field=models.DateField(default='1990-01-01'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-29 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividades',
            old_name='actividadRealizada',
            new_name='actividad_Realizada',
        ),
        migrations.RenameField(
            model_name='monitoria',
            old_name='fechaFinal',
            new_name='fecha_Final',
        ),
        migrations.RenameField(
            model_name='monitoria',
            old_name='fechaInicio',
            new_name='fecha_Inicio',
        ),
    ]

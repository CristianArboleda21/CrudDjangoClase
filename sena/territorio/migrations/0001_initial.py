# Generated by Django 4.0.6 on 2022-07-29 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Monitoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('fechaInicio', models.DateTimeField()),
                ('fechaFinal', models.DateTimeField()),
                ('aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='territorio.aprendiz')),
            ],
        ),
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividadRealizada', models.CharField(max_length=100)),
                ('obs', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='territorio.monitoria')),
            ],
        ),
    ]

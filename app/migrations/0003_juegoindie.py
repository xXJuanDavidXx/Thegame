# Generated by Django 5.0.6 on 2024-07-10 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_usuario_desarollador_juego_descarga_alter_consola_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='JuegoIndie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('desarrollador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juegos', to='app.usuario_desarollador')),
            ],
        ),
    ]

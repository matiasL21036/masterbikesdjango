# Generated by Django 4.2.2 on 2023-06-23 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_mecanico_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenReparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bicicleta_nombre', models.CharField(max_length=100)),
                ('descripcion_problema', models.TextField()),
                ('fecha', models.DateField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.mecanico')),
            ],
        ),
    ]

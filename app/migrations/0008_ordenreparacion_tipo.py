# Generated by Django 4.2.2 on 2023-06-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_ordenreparacion_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenreparacion',
            name='tipo',
            field=models.IntegerField(choices=[('1', 'reparacion'), ('2', 'mantencion')], default=1),
            preserve_default=False,
        ),
    ]
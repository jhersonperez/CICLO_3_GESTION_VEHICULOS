# Generated by Django 4.1.1 on 2022-10-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GESTION_VEHICULOS', '0003_vehiculo_color_vehiculo_kilometros_vehiculo_modelo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

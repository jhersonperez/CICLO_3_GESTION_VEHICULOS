# Generated by Django 4.1.1 on 2022-10-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GESTION_VEHICULOS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
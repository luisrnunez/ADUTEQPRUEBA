# Generated by Django 4.2.3 on 2023-07-27 05:45

import Prestamos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0005_prestamo_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagomensual',
            name='evidencia',
            field=models.FileField(blank=True, null=True, upload_to=Prestamos.models.upload_to_evidencia),
        ),
    ]

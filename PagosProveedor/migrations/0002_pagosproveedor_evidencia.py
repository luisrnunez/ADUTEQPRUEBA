# Generated by Django 4.2.3 on 2023-08-18 06:20

import PagosProveedor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagosProveedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagosproveedor',
            name='evidencia',
            field=models.FileField(blank=True, null=True, upload_to=PagosProveedor.models.upload_to_evidencia),
        ),
    ]

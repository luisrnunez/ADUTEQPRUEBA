# Generated by Django 4.2.4 on 2023-09-08 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0007_prestamo_evidencia_prestamo_fecha_primer_pago_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='tipo',
            field=models.BooleanField(default=False),
        ),
    ]
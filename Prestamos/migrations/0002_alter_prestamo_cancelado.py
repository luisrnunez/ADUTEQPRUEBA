# Generated by Django 4.2.3 on 2023-07-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='cancelado',
            field=models.BooleanField(default=False),
        ),
    ]
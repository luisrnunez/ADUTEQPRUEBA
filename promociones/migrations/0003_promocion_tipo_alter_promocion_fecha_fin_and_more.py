# Generated by Django 4.2.3 on 2023-09-02 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0007_rename_ruc_proveedor_ruc'),
        ('promociones', '0002_promocion_evidencia_alter_promocion_fecha_fin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='tipo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor'),
        ),
    ]
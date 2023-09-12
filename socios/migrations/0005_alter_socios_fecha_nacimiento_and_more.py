# Generated by Django 4.2.3 on 2023-09-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0004_alter_aportaciones_socio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socios',
            name='fecha_nacimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socios',
            name='lugar_nacimiento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socios',
            name='numero_convencional',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='socios',
            name='numero_telefonico',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-31 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('economia', '0003_municipio_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicadorambiental',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='indicadoreconomico',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='indicadorinstitucional',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='indicadorsocial',
            name='municipio',
        ),
        migrations.DeleteModel(
            name='Municipio',
        ),
    ]

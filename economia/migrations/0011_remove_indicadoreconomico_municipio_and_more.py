# Generated by Django 4.1.3 on 2023-01-31 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('economia', '0010_initial'),
    ]

    operations = [
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
            name='IndicadorAmbiental',
        ),
        migrations.DeleteModel(
            name='IndicadorEconomico',
        ),
        migrations.DeleteModel(
            name='IndicadorInstitucional',
        ),
        migrations.DeleteModel(
            name='IndicadorSocial',
        ),
        migrations.DeleteModel(
            name='Municipio',
        ),
    ]

# Generated by Django 2.1.3 on 2019-09-11 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField()),
                ('tipo_despesa', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('formas_pagamento', models.CharField(choices=[('Boleto', 'Boleto'), ('Credito', 'Credito'), ('Debito', 'Debito')], default='Boleto', max_length=2)),
                ('vencimento', models.DateField()),
                ('quitado', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 2.1 on 2019-08-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=600)),
                ('date', models.DateField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
            },
        ),
    ]

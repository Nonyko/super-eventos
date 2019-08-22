# Generated by Django 2.1 on 2019-08-21 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='convidados',
            field=models.ManyToManyField(blank=True, related_name='convidadoemeventos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='evento',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventoscriados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evento',
            name='date',
            field=models.DateTimeField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.CharField(blank=True, max_length=700),
        ),
    ]
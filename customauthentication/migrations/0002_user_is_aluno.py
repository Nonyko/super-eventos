# Generated by Django 2.1 on 2018-08-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauthentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_aluno',
            field=models.BooleanField(default=True),
        ),
    ]
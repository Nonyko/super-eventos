# Generated by Django 2.1 on 2018-08-21 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customauthentication', '0006_user_is_aluno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_aluno',
            new_name='aluno',
        ),
    ]

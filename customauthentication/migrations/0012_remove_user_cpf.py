# Generated by Django 2.1 on 2019-08-21 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customauthentication', '0011_remove_user_is_comum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpf',
        ),
    ]

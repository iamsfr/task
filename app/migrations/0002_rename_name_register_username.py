# Generated by Django 4.1.2 on 2022-12-24 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='name',
            new_name='username',
        ),
    ]

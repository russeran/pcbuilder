# Generated by Django 4.0.4 on 2022-07-22 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='picture',
        ),
    ]

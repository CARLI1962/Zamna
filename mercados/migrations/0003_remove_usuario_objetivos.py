# Generated by Django 2.2 on 2020-05-12 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercados', '0002_auto_20200511_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='objetivos',
        ),
    ]

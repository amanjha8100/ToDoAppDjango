# Generated by Django 3.2.2 on 2021-05-15 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210512_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-pk', 'status']},
        ),
    ]

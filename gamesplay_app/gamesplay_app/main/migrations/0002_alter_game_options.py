# Generated by Django 4.0.4 on 2022-05-18 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('title',)},
        ),
    ]
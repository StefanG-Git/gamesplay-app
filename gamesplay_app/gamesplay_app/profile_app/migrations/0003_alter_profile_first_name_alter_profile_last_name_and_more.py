# Generated by Django 4.0.4 on 2022-05-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_rename_profilemodel_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.URLField(blank=True, null=True, verbose_name='Profile Picture'),
        ),
    ]
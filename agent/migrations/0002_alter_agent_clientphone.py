# Generated by Django 4.2.4 on 2023-08-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='clientphone',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
    ]
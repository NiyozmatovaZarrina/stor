# Generated by Django 4.2.4 on 2023-08-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('Phone_number', models.IntegerField(max_length=20)),
                ('Email', models.CharField(max_length=50, verbose_name='Email')),
                ('Website', models.CharField(max_length=50, verbose_name='Официальный сайт')),
                ('Activate', models.CharField(max_length=50, verbose_name='Аскив')),
            ],
            options={
                'verbose_name': 'Провайдер',
                'verbose_name_plural': 'Провайдеры',
            },
        ),
    ]
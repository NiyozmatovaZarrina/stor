# Generated by Django 4.2.4 on 2023-08-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.IntegerField(verbose_name='Пароль'),
        ),
    ]
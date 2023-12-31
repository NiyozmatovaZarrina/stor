# Generated by Django 4.2.4 on 2023-08-11 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_alter_user_password'),
        ('storage', '0002_alter_provider_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prihod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalprice', models.FloatField(max_length=100, verbose_name='Цена')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Названиепоставщика', to='storage.provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Пользователь', to='users.user')),
            ],
            options={
                'verbose_name': 'Проход',
                'verbose_name_plural': 'Приходы',
            },
        ),
    ]

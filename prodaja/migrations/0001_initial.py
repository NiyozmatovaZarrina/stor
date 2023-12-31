# Generated by Django 4.2.4 on 2023-08-10 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0002_alter_agent_clientphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100, verbose_name='Название')),
                ('totalprice', models.IntegerField(verbose_name='Цена')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='agent.agent')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажы',
            },
        ),
    ]

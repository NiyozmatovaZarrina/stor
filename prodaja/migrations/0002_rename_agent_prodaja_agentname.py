# Generated by Django 4.2.4 on 2023-08-10 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prodaja', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodaja',
            old_name='agent',
            new_name='agentname',
        ),
    ]
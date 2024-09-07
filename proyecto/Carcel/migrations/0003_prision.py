# Generated by Django 5.1 on 2024-09-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carcel', '0002_alter_policia_options_alter_presos_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Agregar prision',
                'verbose_name_plural': 'Agregar prisiones',
            },
        ),
    ]

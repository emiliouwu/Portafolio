# Generated by Django 2.2.4 on 2021-12-08 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuario', '0004_usuario_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateField(auto_now=True),
        ),
    ]

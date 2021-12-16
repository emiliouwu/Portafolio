# Generated by Django 2.0.6 on 2021-12-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuario', '0005_usuario_fecha_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
            ],
        ),
    ]

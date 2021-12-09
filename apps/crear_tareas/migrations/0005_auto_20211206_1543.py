# Generated by Django 2.2.4 on 2021-12-06 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuario', '0003_auto_20211206_1539'),
        ('crear_tareas', '0004_auto_20211206_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crear_tarea',
            fields=[
                ('id_tarea', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_de_la_tarea', models.CharField(max_length=30)),
                ('fecha_c_tarea', models.DateField(auto_now=True)),
                ('fecha_entrega', models.DateField()),
                ('especificacion', models.CharField(max_length=100, null=True)),
                ('tarea_relacion', models.CharField(max_length=30, null=True)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuario.Usuario')),
            ],
            options={
                'verbose_name': 'Crear tarea',
                'verbose_name_plural': 'Crear tareas',
            },
        ),
        migrations.DeleteModel(
            name='C_tarea',
        ),
    ]

from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario= models.CharField("Nombre de Usuario",unique = True, max_length=30, blank = False)
    correo= models.EmailField("Correo Electronico ",unique = True, max_length=30)
    nombres= models.CharField("Nombres", max_length=30, blank = False, null=True)
    apellidos= models.CharField("Apellidos", max_length=30, blank = False, null=True)
    estado = models.BooleanField("Estado", default = True)
    usuario_funcionario = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    usuario_diseñador_procesos = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now=True, auto_now_add=False)
    

class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre_user']


def __str__(self):
    return self.nombre_user


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length= 90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)





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
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['nombre_usuario']


    def __str__(self):
        return self.nombre_usuario


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length= 90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)



class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    nombre_tarea = models.CharField(max_length=30, blank= False, null= False)
    # para hacer la FK
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_entrega= models.DateField(blank= False, null= False)
    especificacion = models.CharField(max_length=100, blank= False, null= True)
    tarea_relacion = models.CharField(max_length=30, blank= False, null= True)
    
    

    class Meta:
        verbose_name = 'tarea' 
        verbose_name_plural = 'tareas' 

    def __str__(self):
        return self.nombre_tarea

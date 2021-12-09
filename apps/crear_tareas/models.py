from django.db import models
from apps.gestion_usuario.models import Usuario

class Crear_tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    nombre_de_la_tarea = models.CharField(max_length=30, blank= False, null= False)
    # para hacer la FK
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_c_tarea = models.DateField(auto_now=True, auto_now_add=False)
    fecha_entrega= models.DateField(blank= False, null= False)
    especificacion = models.CharField(max_length=100, blank= False, null= True)
    tarea_relacion = models.CharField(max_length=30, blank= False, null= True)
    
    

    class Meta:
        verbose_name = 'Crear tarea' 
        verbose_name_plural = 'Crear tareas' 

    def _str_(self):
        return self.nom_tarea
from django.contrib import admin
from .models import Usuario     
from .models import Tarea

admin.site.register(Tarea)



class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombre', 'apellidos', 'correo')



admin.site.register(Usuario)



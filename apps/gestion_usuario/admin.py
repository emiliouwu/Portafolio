from django.contrib import admin
from .models import Usuario     


class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombre', 'apellidos', 'correo')



admin.site.register(Usuario)



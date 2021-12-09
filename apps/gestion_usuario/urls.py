from django.urls import path, re_path
from .views import crearUsuario, listarUsuario, editarUsuario, eliminarUsuario

urlpatterns = [
        path('crear_usuario/', crearUsuario, name = 'crear_usuario'),
        path('listar_usuario/', listarUsuario, name = 'listar_usuario'),
        path('editar_usuario/<int:id_usuario>',editarUsuario, name = 'editar_usuario'),
        path('eliminar_usuario/<int:id_usuario>',eliminarUsuario, name = 'eliminar_usuario')


]
# re_path(r'^crear_usuario/(?P<id>\d+)',crearUsuario, name = "csskf")
# path('listar_usuario/<slug:titulo>/<int:pk>', listarUsuario, name = 'listar_usuario'),
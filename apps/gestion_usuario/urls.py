from django.urls import path, re_path
from .views import  Home, crearUsuario, listarUsuario, editarUsuario, eliminarUsuario
from .views import crearTarea, listarTarea, editarTarea, eliminarTarea
from apps.gestion_usuario import views
from .views import crearTarea


urlpatterns = [
        
        path ('',Home, name = 'index'),
        path('crear_usuario/', crearUsuario, name = 'crear_usuario'),
        path('listar_usuario/', listarUsuario, name = 'listar_usuario'),
        path('editar_usuario/<int:id_usuario>',editarUsuario, name = 'editar_usuario'),
        path('eliminar_usuario/<int:id_usuario>',eliminarUsuario, name = 'eliminar_usuario'),
        path('usuario_pdf', views.usuario_pdf, name='usuario_pdf'),
        path('crear_tarea/', crearTarea, name = 'crear_tarea'),
        path('listar_tarea/', listarTarea, name = 'listar_tarea'),
        path('editar_tarea/<int:id_tarea>',editarTarea, name = 'editar_tarea'),
        path('eliminar_tarea/<int:id_tarea>',eliminarTarea, name = 'eliminar_tarea'),
        path('tarea_pdf', views.tarea_pdf, name='tarea_pdf'),
]




# re_path(r'^crear_usuario/(?P<id>\d+)',crearUsuario, name = "csskf")
# path('listar_usuario/<slug:titulo>/<int:pk>', listarUsuario, name = 'listar_usuario'),

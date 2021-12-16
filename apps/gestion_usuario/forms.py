from django import forms
from .models import Usuario
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre_tarea', 'responsable', 'fecha_entrega',
                    'especificacion', 'tarea_relacion']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo', 'nombres', 'apellidos', 
        'usuario_funcionario' , 'usuario_administrador' ,'usuario_diseñador_procesos']
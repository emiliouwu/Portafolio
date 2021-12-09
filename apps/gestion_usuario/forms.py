from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo', 'nombres', 'apellidos', 
        'usuario_funcionario' , 'usuario_administrador' ,'usuario_diseñador_procesos']
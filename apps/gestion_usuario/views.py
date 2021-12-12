from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from apps.gestion_usuario.utils import render_a_pdf
from .models import Usuario
from .forms import UsuarioForm
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View

def Home(request):
    return render(request,'index.html')

def crearUsuario(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('index')
        
    else:
            usuario_form = UsuarioForm()
    return render(request,'gestion_usuario/crear_usuario.html',{'usuario_form':usuario_form})

def listarUsuario(request):
    usuarios = Usuario.objects.filter(estado = True)
    return render(request, 'gestion_usuario/listar_usuario.html', {'usuarios':usuarios})

class listarUsuariosPdf(View):
    
    def get(self, request. *args, **kwags):
        usuarios = Usuario.objects.all()
        data = {
            'usuarios':usuarios
        }
        pdf = render_a_pdf('gestion_usuario/listar_usuario.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def editarUsuario(request, id_usuario):
    usuario_form = None
    error = None
    try:
        usuario = Usuario.objects.get(id_usuario = id_usuario)
        if request.method =='GET':
            usuario_form = UsuarioForm(instance=usuario)
        else:
            usuario_form = UsuarioForm(request.POST, instance = usuario)
            if usuario_form.is_valid():
                usuario_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request,'gestion_usuario/crear_usuario.html',{'usuario_form':usuario_form, 'error':error})

def eliminarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario = id_usuario)
    if request.method == 'POST':
        usuario.estado = False
        usuario.save()
        return redirect('gestion_usuario:listar_usuario')
    return render(request,'gestion_usuario/eliminar_usuario.html', {'usuario':usuario})


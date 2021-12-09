from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm
from django.core.exceptions import ObjectDoesNotExist


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


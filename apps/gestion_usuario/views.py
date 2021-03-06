from django.shortcuts import redirect, render
from .models import Usuario, Tarea
from .forms import UsuarioForm, TareaForm
from django.core.exceptions import ObjectDoesNotExist

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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
        usuario.delete()
        return redirect('gestion_usuario/listar_usuario.html')
    return render(request,'gestion_usuario/eliminar_usuario.html', {'usuario':usuario})

def usuario_pdf(request):

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    usuarios = Usuario.objects.all()

    lines = []

    for usuario in usuarios:
        lines.append(usuario.nombre_usuario)
        lines.append(usuario.correo)
        lines.append(usuario.nombres)
        lines.append(usuario.apellidos)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)


    return FileResponse(buf, as_attachment=True, filename='usuario.pdf')



def crearTarea(request):
    if request.method == 'POST':
        tarea_form = TareaForm(request.POST)
        if tarea_form.is_valid():
            tarea_form.save()
            return redirect('index')

    else:
            tarea_form = TareaForm()
    return render(request,'gestion_usuario/crear_tarea.html',{'tarea_form':tarea_form})

def listarTarea(request):
    tareas = Tarea.objects.all()
    return render(request, 'gestion_usuario/listar_tarea.html', {'tareas':tareas})


def editarTarea(request, id_tarea):
    tarea_form = None
    error = None
    try:
        tarea = Tarea.objects.get(id_tarea = id_tarea)
        if request.method =='GET':
            tarea_form = TareaForm(instance=tarea)
        else:
            tarea_form = TareaForm(request.POST, instance = tarea)
            if tarea_form.is_valid():
                tarea_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request,'gestion_usuario/crear_tarea.html',{'tarea_form':tarea_form, 'error':error})

def eliminarTarea(request, id_tarea):
    tarea = Tarea.objects.get(id_tarea = id_tarea)
    if request.method == 'POST':
        tarea.delete()
        return redirect('gestion_usuario/listar_tarea.html')
    return render(request,'gestion_usuario/eliminar_tarea.html', {'tarea':tarea})
    

def tarea_pdf(request):

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    tareas = Tarea.objects.all()

    lines = []

    for tarea in tareas:
        lines.append(tarea.nombre_tarea)
        lines.append(tarea.responsable)
        lines.append(tarea.nombres)
        lines.append(tarea.apellidos)
        lines.append("========================")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)


    return FileResponse(buf, as_attachment=True, filename='tarea.pdf')
from django.shortcuts import render
from universidad.Models.Alumno.models import Alumno

def dashboard(request):
    context = {
        'total_alumnos': Alumno.objects.count(),
        'activos': Alumno.objects.filter(is_active=True).count(),
        'inactivos': Alumno.objects.filter(is_active=False).count(),
    }
    return render(request, 'core/dashboard.html', context)

def cursos(request):
    return render(request, 'curso/list.html')

def calificaciones(request):
    return render (request,
                   'calificaciones/list.html')

def catedraticos(request):
    return render(request, 'catedraticos/list.html')

def asignacion_curso(request):
    return render(request, 'asignacion_curso/list.html')

def inscripcion_alumno(request):
    return render(request, 'inscripcion_alumno/list.html')

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from App import forms, models

# Create your views here.

# def index(request):

#     plantilla = loader.get_template('index.html')

#     documento = plantilla.render() # renderizo la plantilla en la variable documento

#     return HttpResponse(documento)

def index(request):
    return render(request, 'index.html')

# def educacion(request):
#     return render(request, 'educacion.html' )

# def educacion(request):

#     plantilla = loader.get_template('educacion.html')

#     documento = plantilla.render() # renderizo la plantilla en la variable documento

#     return HttpResponse(documento)

# def actividades(request):
#      return render(request, 'actividades.html' )

# def actividades(request):

#     plantilla = loader.get_template('actividades.html')

#     documento = plantilla.render() # renderizo la plantilla en la variable documento

#     return HttpResponse(documento)

# def laboral(request):
#     return render(request, 'laboral.html' )

# def laboral(request):

#     plantilla = loader.get_template('laboral.html')

#     documento = plantilla.render() # renderizo la plantilla en la variable documento

#     return HttpResponse(documento)

def educacion(request):
    if request.method == 'POST':
        mi_formulario = forms.Formulario_educacion(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            educacion = models.Educacion(nivel = informacion['nivel'], establecimiento = informacion['establecimiento'], estado = informacion['estado'])
            educacion.save()
            return render(request, 'index.html')
        
    else:
        mi_formulario = forms.Formulario_educacion()
        return render(request, 'educacion.html', {'mi_formulario': mi_formulario})

def actividades(request):
    if request.method == 'POST':
        mi_formulario = forms.Formulario_actividades(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            actividades = models.Actividades(tipo = informacion['tipo'], nombre = informacion['nombre'], fecha = informacion['fecha'])
            actividades.save()
            return render(request, 'index.html')
        
    else:
        mi_formulario = forms.Formulario_actividades()
        return render(request, 'actividades.html', {'mi_formulario': mi_formulario})
    
def laboral(request):
    if request.method == 'POST':
        mi_formulario = forms.Formulario_laboral(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            laboral = models.Laboral(nombre = informacion['nombre'], empresa = informacion['empresa'], rubro = informacion['rubro'])
            laboral.save()
            return render(request, 'index.html')
        
    else:
        mi_formulario = forms.Formulario_laboral()
        return render(request, 'laboral.html', {'mi_formulario': mi_formulario})
    
def buscar(request):
    valorBuscado = request.GET['nivel']
    estudios = models.Educacion.objects.filter(nivel__icontains = valorBuscado)
    return render(request, 'index.html', {'estudios':estudios, 'valorBuscado':valorBuscado})
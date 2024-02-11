from django import forms

class Formulario_educacion(forms.Form):

    nivel = forms.CharField()
    establecimiento = forms.CharField()
    estado = forms.CharField()

class Formulario_actividades(forms.Form):

    tipo = forms.CharField(max_length=30)
    nombre = forms.CharField(max_length=30)
    fecha = forms.DateField()

class Formulario_laboral(forms.Form):

    nombre = forms.CharField()
    empresa = forms.CharField()
    rubro = forms.CharField()
# TuPrimeraPagina+MartinezCaballero

# ---Modelos:---

Educacion, que posee 3 atributos:
nivel: Universidad, Curso, etc.
establecimiento: Entidad donde se cursa.
estado: En progreso o finzalizado.

Actividades:
tipo: Deporte, Hobby, etc.
nombre: nombre de la actividad.
fecha: fecha de inicio.

Laboral:
nombre: nombre del empleo.
empresa: nombre de la empresa.
rubro: nombre del rubro.


# ---Templates:---

  Base.html, template padre, del cual heredan las siguientes plantillas:

  Index/ Página principal:

Se encunetra el buscador por nivel educativo, que busca en la clase Educacion. Los niveles son: Universidad o Curso.

Por defecto se muestra la vista "index" que renderiza el archivo "index.html" .Al utilizar el buscador se muestra la vista "buscar" que renderiza el archivo "index.html" pero con el contexto que estoy buscando en la base de datos, para mostrar los resultados de dicha busquedad. Ambas vistas se encuentran en el archivo views.py, dentro de la App.

  educacion/actividades/laboral.html, ingreso de datos:

Cada una de estas plantillas cuentan con su formulario correspondiente, los cuales se encuentran en el archivo forms.py, y están asociadas a las vistas educacion/actividades y laboral segun corresponda, dentro del archivo views.py, ubicado dentro de la App.

# ---Utilizacion---

Carga de en la base de datos las clases: educacion, actividades y laboral, dentro de c/u de las plantilla a las cuales se acceden desde la barra de navegación.
Consulta a la base de datos, sobre la clase educacion, desde la página principal.


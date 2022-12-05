# Pasos para poder implementar formulario
Partiendo del siguiente ejemplo [clase_19_portfolio_django_mondelos_y_templates.md](clase_19_portfolio_django_mondelos_y_templates.md), Vamos a implementar un formulario:

- Primero tenemos que crear un nuevo modulo python dentro del paquete ejemplo con el nombre, `forms.py`
  en el copiamos lo siguiente:
  
  ```python
  from django import forms
  class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)
  ```

- Segundo Creamos un template en `ejemplo/templates/ejemplo` con el nombre `buscar.html`, y colocamos el siguiente código:
  ```html
  <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>buscar familiar por nombre</h1>
      
        <form action="/mi-familia/buscar" method="post">
          {% csrf_token %}
          {{ form }}
          <input type="submit" value="Submit">
        </form>

        {% for familiar in lista_familiares %}
        <ul>
            <li> Nombre: {{familiar.nombre}}, Dirección: {{familiar.direccion}}, Pasaporte: {{familiar.numero_pasaporte}}</li>
        </ul>
        {% endfor %}

    </body>
    </html>
  ``` 

- Tercero vamos a definir una vista basada en clases, para ello tenemos que hacer:
  - En la parte superior de `ejemplo/views.py` importamos lo siguiente:
    ```python
    from django.shortcuts import render
    from ejemplo.models import Familiar
    from ejemplo.forms import Buscar # <--- NUEVO IMPORT
    from django.views import View # <-- NUEVO IMPORT 
    ```
  - En la parte inferior de `ejemplo/views.py` agregamos una nueva clase, que hereda de View, copiamos lo siguiente :
    ```python
    class BuscarFamiliar(View):
        form_class = Buscar
        template_name = 'ejemplo/buscar.html'
        initial = {"nombre":""}
        def get(self, request):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form})
        def post(self, request):
            form = self.form_class(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get("nombre")
                lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form':form, 
                                                            'lista_familiares':lista_familiares})
            return render(request, self.template_name, {"form": form})
    ```
  - Cuarto tenemos que routear la vista con una nueva url en `project/urls.py`:
    ```python
      from django.contrib import admin
      from django.urls import path
      from ejemplo.views import (index, index_dos, index_tres, 
                                imc, monstrar_familiares, BuscarFamiliar)
      from blog.views import index as blog_index
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('saludar/', index),
          path('saludar/<nombre>/<apellido>/', index_dos),
          path('mostrar-notas/', index_tres),
          path('imc/<int:peso>/<int:altura>', imc),
          path('mi-familia/', monstrar_familiares),
          path('blog/', blog_index),
          path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
      ]
    ```

# Pasos para implementar Herencia de templates

- Para poder implementar herencia de templates, primero tenemos que crear un template `base.html` dentro de `ejemplo/templates/ejemplo`
  ```html
  <!DOCTYPE html>
  <html lang="en">

  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  </head>

  <body>
      <h1> Mi Pagina de Familiares </h1>
      <h2>{% block titulo %}{% endblock %}<h2>
      {% block contenido %}{% endblock %}
  </body>

  </html>
  ```

  - Vamos a modificar el template, `familiares.html`, les tendria que quedar así:

    ```html
    {% extends 'ejemplo/base.html' %}
    {% block titulo%} Lista de todos mis Familiares {% endblock %}
    {% block contenido %}
      {% for familiar in lista_familiares %}
          <ul>
              <li> Nombre: {{familiar.nombre}}, Dirección: {{familiar.direccion}}, Pasaporte: {{familiar.numero_pasaporte}}</li>
          </ul>
      {% endfor %}
    {% endblock %}
    ```

  - Ahora vamos hacer lo mismo con el template, `buscar.html` que creamos anteriormente, reemplazar el contenido de ese template por:

    ```html
    {% extends 'ejemplo/base.html' %}
    {% block titulo%} Buscar Familiares por nombre {% endblock %}
    {% block contenido %}
      
      <form action="/mi-familia/buscar" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
      </form>

      {% for familiar in lista_familiares %}
          <ul>
              <li> Nombre: {{familiar.nombre}}, Dirección: {{familiar.direccion}}, Pasaporte: {{familiar.numero_pasaporte}}</li>
          </ul>
      {% endfor %}
    {% endblock %}
    ```

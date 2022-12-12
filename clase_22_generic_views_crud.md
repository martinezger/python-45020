# Pasos para poder implementar generic views CRUD
Partiendo del siguiente ejemplo [clase_21_formulario_de_actualizar.md](clase_21_formulario_de_actualizar.md), Vamos a implementar las vistas genéricas para hacer crud que django trae:

### LIST VIEW

- Vamos a crear un template en `ejemplo/templates/ejemplo` con el nombre `familiar_list.html` y agregamos lo siguiente:
  
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
  <ul>

  {% block buscar %} {% endblock %}

  {% for familiar in object_list %}
      <li>{{familiar}}</li>
  {% endfor %}    
  </ul>

  </body>
  </html>
  ```

- Segundo vamos a definir una vista basada en clases para crear un familiar, para ello:
  
    - Tenemos que importar la vista generica de cración, con lo cual en la parte superior:

      ```python
      from django.shortcuts import render, get_object_or_404
      from ejemplo.models import Familiar
      from ejemplo.forms import Buscar, FamiliarForm
      from django.views import View 
      from django.views.generic import ListView # <----- NUEVO IMPORT
      ```

   
  - En la parte inferior de `ejemplo/views.py` agregamos una nueva clase, que hereda de CreateView, copiamos lo siguiente :
    
    ```python
    class FamiliarList(ListView):
      model = Familiar
    ```
  - Tercero tenemos que routear la vista con una nueva url en `project/urls.py`:
    
    ```python
      from django.contrib import admin
      from django.urls import path
      from ejemplo.views import (index, index_dos, index_tres, 
                                imc, monstrar_familiares, BuscarFamiliar, 
                                AltaFamiliar, ActualizarFamiliar, FamiliarList) # <--- NUEVO IMPORT
      from blog.views import index as blog_index

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('saludar/', index),
          path('saludar/<nombre>/<apellido>/', index_dos),
          path('mostrar-notas/', index_tres),
          path('imc/<int:peso>/<int:altura>', imc),
          path('mi-familia/', monstrar_familiares),
          path('blog/', blog_index),
          path('mi-familia/buscar', BuscarFamiliar.as_view()), 
          path('mi-familia/alta', AltaFamiliar.as_view()),
          path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), 
          path('panel-familia/', FamiliarList.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR

      ]
    ```


### CREATE VIEW

- Vamos a crear un template en `ejemplo/templates/ejemplo` con el nombre `familiar_form.html` y agregamos lo siguiente:
  
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

      <form method="post">
          {% csrf_token %}
          {{form.as_p}}
          <input type="submit" value="agregar">
      </form>

  </body>
  </html>
  ``` 

- Segundo vamos a definir una vista basada en clases para crear un familiar, para ello:
  
    - Tenemos que importar la vista generica de cración, con lo cual en la parte superior:

      ```python
      from django.shortcuts import render, get_object_or_404
      from ejemplo.models import Familiar
      from ejemplo.forms import Buscar, FamiliarForm
      from django.views import View 
      from django.views.generic import ListView, CreateView # <----- NUEVO IMPORT
      ```

   
  - En la parte inferior de `ejemplo/views.py` agregamos una nueva clase, que hereda de CreateView, copiamos lo siguiente :
    ```python
    class FamiliarCrear(CreateView):
      model = Familiar
      success_url = "/panel-familia"
      fields = ["nombre", "direccion", "numero_pasaporte"]
    ```
  - Tercero tenemos que routear la vista con una nueva url en `project/urls.py`:
    
    ```python
      from django.contrib import admin
      from django.urls import path
      from ejemplo.views import (index, index_dos, index_tres, 
                                imc, monstrar_familiares, BuscarFamiliar, 
                                AltaFamiliar, ActualizarFamiliar, FamiliarCrear) # <--- NUEVO IMPORT
      from blog.views import index as blog_index

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('saludar/', index),
          path('saludar/<nombre>/<apellido>/', index_dos),
          path('mostrar-notas/', index_tres),
          path('imc/<int:peso>/<int:altura>', imc),
          path('mi-familia/', monstrar_familiares),
          path('blog/', blog_index),
          path('mi-familia/buscar', BuscarFamiliar.as_view()), 
          path('mi-familia/alta', AltaFamiliar.as_view()),
          path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
          path('panel-familia/', FamiliarList.as_view()), 
          path('panel-familia/crear', FamiliarCrear.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR

      ]
    ```

### DELETE VIEW

- Vamos a crear un template en `ejemplo/templates/ejemplo` con el nombre `familiar_confirm_delete.html` y agregamos lo siguiente:
  
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

      <form method="post">
          {% csrf_token %}
          "¿ Estás seguro de borrar el familiar {{ object }} ?"
          <input type="submit" value="SI">
      </form>

  </body>
  </html>
  ``` 

- Segundo vamos a definir una vista basada en clases para borrar un familiar, para ello:
  
    - Tenemos que importar la vista generica de borrado, con lo cual en la parte superior:

      ```python
      from django.shortcuts import render, get_object_or_404
      from ejemplo.models import Familiar
      from ejemplo.forms import Buscar, FamiliarForm
      from django.views import View 
      from django.views.generic import ListView, CreateView, DeleteView # <----- NUEVO IMPORT
      ```

   
  - En la parte inferior de `ejemplo/views.py` agregamos una nueva clase, que hereda de DeleteView, copiamos lo siguiente :
    
    ```python
    class FamiliarBorrar(DeleteView):
      model = Familiar
      success_url = "/panel-familia"
    ```

  - Tercero tenemos que routear la vista con una nueva url en `project/urls.py`:
    
    ```python
      from django.contrib import admin
      from django.urls import path
      from ejemplo.views import (index, index_dos, index_tres, 
                                imc, monstrar_familiares, BuscarFamiliar, 
                                AltaFamiliar, ActualizarFamiliar, FamiliarCrear) # <--- NUEVO IMPORT
      from blog.views import index as blog_index

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('saludar/', index),
          path('saludar/<nombre>/<apellido>/', index_dos),
          path('mostrar-notas/', index_tres),
          path('imc/<int:peso>/<int:altura>', imc),
          path('mi-familia/', monstrar_familiares),
          path('blog/', blog_index),
          path('mi-familia/buscar', BuscarFamiliar.as_view()), 
          path('mi-familia/alta', AltaFamiliar.as_view()),
          path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
          path('panel-familia/', FamiliarList.as_view()), 
          path('panel-familia/crear', FamiliarCrear.as_view()),
          path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
      ]
    ```

### UPDATE VIEW

- Como el formulario para actualizar, en este caso particular, es el mismo que el de crear no necesitamos agregar un nuevo template.
  

- Segundo vamos a definir una vista basada en clases para actualizar un familiar, para ello:
  
    - Tenemos que importar la vista generica de actualización, con lo cual en la parte superior:

      ```python
      from django.shortcuts import render, get_object_or_404
      from ejemplo.models import Familiar
      from ejemplo.forms import Buscar, FamiliarForm
      from django.views import View 
      from django.views.generic import ListView, CreateView, DeleteView, UpdateView # <----- NUEVO IMPORT
      ```

   
  - En la parte inferior de `ejemplo/views.py` agregamos una nueva clase, que hereda de UpdateView, copiamos lo siguiente :
    
    ```python
    class FamiliarActualizar(UpdateView):
      model = Familiar
      success_url = "/panel-familia"
      fields = ["nombre", "direccion", "numero_pasaporte"]
    ```

  - Tercero tenemos que routear la vista con una nueva url en `project/urls.py`:
    
    ```python
      from django.contrib import admin
      from django.urls import path
      from ejemplo.views import (index, index_dos, index_tres, 
                                imc, monstrar_familiares, BuscarFamiliar, 
                                AltaFamiliar, ActualizarFamiliar, FamiliarCrear) # <--- NUEVO IMPORT
      from blog.views import index as blog_index

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('saludar/', index),
          path('saludar/<nombre>/<apellido>/', index_dos),
          path('mostrar-notas/', index_tres),
          path('imc/<int:peso>/<int:altura>', imc),
          path('mi-familia/', monstrar_familiares),
          path('blog/', blog_index),
          path('mi-familia/buscar', BuscarFamiliar.as_view()), 
          path('mi-familia/alta', AltaFamiliar.as_view()),
          path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
          path('panel-familia/', FamiliarList.as_view()), 
          path('panel-familia/crear', FamiliarCrear.as_view()),
          path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), 
          path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
      ]
    ```

    


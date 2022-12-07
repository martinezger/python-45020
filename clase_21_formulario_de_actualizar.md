# Pasos para poder implementar formulario actualizar un modelo
Partiendo del siguiente ejemplo [clase_21_formulario_de_carga.md](clase_21_formulario_de_carga.md), Vamos a implementar un formulario para actualizar el modelo Familar:

- Para el caso de la actualización no hace falta crear una nueva clase formulario ya que la actulización utiliza el mismo
  formulario que el alta.
  
- Primero Creamos un template en `ejemplo/templates/ejemplo` con el nombre `actulizar_familiar.html`, y colocamos el siguiente código, prestar atención que estamos herendando de `base.html`:
  ```html
  {% extends 'ejemplo/base.html' %}
  {% block titulo%} Modificar un Familiar {% endblock %}
  {% block contenido %}

  <!-- Prestar aatención a la variable familiar.id -->
  <form action="/mi-familia/actualizar/{{ familiar.id }}" method="post"> 
      {% csrf_token %}
      {{ form }}
      <input type="submit" value="Submit">
  </form>

  <h2 style="color:green">{{msg_exito}}</h2>

  {% endblock %}
  ``` 

- Segundo vamos a definir una vista basada en clases para modificar un familiar, para ello:
  
    - Como ya tenemos importado el Formulario de FamiliarForm para este caso no tenemos que volver a importar, pero vamos a usar una nueva function de django que se llama get_object_or_404 para eso lo importamos en la parte superior:

      ```python
      from django.shortcuts import render, get_object_or_404 # <----- Nuevo import
      from ejemplo.models import Familiar
      from ejemplo.forms import Buscar, FamiliarForm
      from django.views import View 
      ```

   
  - En la parte inferior de `ejemplo/views.py` agregamos una nueva clase, que hereda de View, copiamos lo siguiente :
    ```python
    class ActualizarFamiliar(View):
      form_class = FamiliarForm
      template_name = 'ejemplo/actualizar_familiar.html'
      initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
      
      # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
      def get(self, request, pk): 
          familiar = get_object_or_404(Familiar, pk=pk)
          form = self.form_class(instance=familiar)
          return render(request, self.template_name, {'form':form,'familiar': familiar})

      # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
      def post(self, request, pk): 
          familiar = get_object_or_404(Familiar, pk=pk)
          form = self.form_class(request.POST ,instance=familiar)
          if form.is_valid():
              form.save()
              msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
              form = self.form_class(initial=self.initial)
              return render(request, self.template_name, {'form':form, 
                                                          'familiar': familiar,
                                                          'msg_exito': msg_exito})
          
          return render(request, self.template_name, {"form": form})
    ```
  - Tercero tenemos que routear la vista con una nueva url en `project/urls.py`:
    
    ```python
      from django.contrib import admin
      from django.urls import path
      from ejemplo.views import (index, index_dos, index_tres, 
                                imc, monstrar_familiares, BuscarFamiliar, 
                                AltaFamiliar, ActualizarFamiliar) # <--- NUEVO IMPORT
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
          # EL paramatro pk hace referencia al identificador único en la base de datos para Familiar.
          path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
      ]
    ```

  - Cuarto tenemos que hacer una modificación a el template de `familiares.html` para que nos aparezca la opción de 
    modificación, con lo cual reemplazamos en `ejemplo/templates/ejemplo/familiares.html` con lo siguiente:

    ```html
    {% extends 'ejemplo/base.html' %}
    {% block contenido %}
    {% for familiar in lista_familiares %}
    <ul>
        <li> Nombre: {{familiar.nombre}}, Dirección: {{familiar.direccion}}, Pasaporte: {{familiar.numero_pasaporte}}
            <!-- Esto agrega un link al form de actulización-->
            <a href='actualizar/{{ familiar.id }}'>Actualizar</a>
        </li>
    </ul>
    {% endfor %}
    {%endblock %}

    {% block titulo%}
    Lista de todos mis Familiares
    {% endblock %}
    ```    

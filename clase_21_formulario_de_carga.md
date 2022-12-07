# Pasos para poder implementar formulario de carga para modelos
Partiendo del siguiente ejemplo [clase_20_herencia_y_formularios.md](clase_20_herencia_y_formularios.md), Vamos a implementar un formulario para cargar el modelo Familar:

- Primero creamos un clase AltaFamiliar en `ejemplo/forms.py` en el copiamos lo siguiente:
  
  ```python
  from django import forms
  from ejemplo.models import Familiar
  
  class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
  
  class FamiliarForm(forms.ModelForm):
    class Meta:
      model = Familiar
      fields = ['nombre', 'direccion', 'numero_pasaporte']
  ```

- Segundo Creamos un template en `ejemplo/templates/ejemplo` con el nombre `alta_familiar.html`, y colocamos el siguiente código, prestar atención que estamos herendando de `base.html`:
  ```html
  {% extends 'ejemplo/base.html' %}
  {% block titulo%} Alta de nuevo Familiar {% endblock %}
  {% block contenido %}
    
    <form action="/mi-familia/alta" method="post">
      {% csrf_token %}
      {{ form }}
      <input type="submit" value="Submit">
    </form>

    <h2 style="color:green">{{msg_exito}}</h2>
  
  {% endblock %}
  ``` 

- Tercero vamos a definir una vista basada en clases para cargar un familiar, para ello tenemos que hacer:
  - En la parte superior de `ejemplo/views.py` importamos lo siguiente:
    ```python
    from django.shortcuts import render
    from ejemplo.models import Familiar
    from ejemplo.forms import Buscar, FamiliarForm #<--- NUEVO IMPORT
    from django.views import View 
    ```
  - En la parte inferior de `ejemplo/views.py` agregamos una nueva clase, que hereda de View, copiamos lo siguiente :
    ```python
    class AltaFamiliar(View):

        form_class = FamiliarForm
        template_name = 'ejemplo/alta_familiar.html'
        initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

        def get(self, request):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form})

        def post(self, request):
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
                form = self.form_class(initial=self.initial)
                return render(request, self.template_name, {'form':form, 
                                                            'msg_exito': msg_exito})
            
            return render(request, self.template_name, {"form": form})

    ```
  - Cuarto tenemos que routear la vista con una nueva url en `project/urls.py`:
    ```python
      from django.contrib import admin
      from django.urls import path
      from ejemplo.views import (index, index_dos, index_tres, 
                                imc, monstrar_familiares, BuscarFamiliar, AltaFamiliar)#<--- NUEVO IMPORT
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
          path('mi-familia/alta', AltaFamiliar.as_view()) # NUEVA RUTA PARA BUSCAR FAMILIAR
      ]

    ```

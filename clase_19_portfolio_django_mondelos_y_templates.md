# Pasos para poder Crear un modelo y renderizar el contenido mediante un template django 

Partiendo del siguiente ejemplo [clase_18_portfolio_django.md](clase_18_portfolio_django.md)

- Abrimos el archivo ejemplo/models.py y agregamos el siguiente codigo:
  
  ```python
  from django.db import models
    class Familiar(models.Model):
        nombre = models.CharField(max_length=100)
        direccion = models.CharField(max_length=200)
        numero_pasaporte = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"
  ```

- Luego abrimos el archivo ejemplos/views.py y agregamos en la parte superior del archivo los imports:
  ```python
    from django.shortcuts import render
    from ejemplo.models import Familiar
  ```
  
  y al final del archivo la vista para renderizar la lista de familiares: 
  
  ```python
  def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})
  ```
- Tenemos que agregar un template para poder mostrar una lista, crear un archivo en ejemplo/templates/ejemplo con 
  el nombre `familiares.html` y en el agregar:
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

      <h1>Lista de mis familiares</h1>

      {% for familiar in lista_familiares %}
          <ul>
              <li> Nombre: {{familiar.nombre}}, Dirección: {{familiar.direccion}}, Pasaporte: {{familiar.numero_pasaporte}} </li>
          </ul>
      {% endfor %}
      
  </body>
  </html>
  ```

- Ahora abrimos project/urls.py para poder routear la nueva vista, con el siguiente código:
  ```python
    from django.contrib import admin
    from django.urls import path
    from ejemplo.views import index, index_dos, index_tres, monstrar_familiares
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('saludar/', index),
        path('saludar/<nombre>/<apellido>/', index_dos),
        path('mostrar-notas/', index_tres),
        path('mi-familia/', monstrar_familiares), # nueva vista
    ]
   
  ```

- Como se agrego un nuevo modelo es necesario generar una migration de la base de datos, para ello tienen que hacer 
 lo siguiente en la terminal de visual studio code:

 ```bash
 python manage.py makemigrations
 ```
 y luego
 ```bash
 python manage.py migrate
 ```

 - Para probar si todo fue bien, hay que correr el servidor de pruebas:
  
```bash
python manage.py runserver
```
y para poder abrir la vista que creamos pueden ir a [http://127.0.0.1:8000/mi-familia](http://127.0.0.1:8000/mi-familia)
  

la lista seguro aparece vacía asi que vamos a crear un pequeño script de carga y lo vamos a dejar dentro del carpeta raiz 
del proyecto, le ponemos como nombre al archivo `seed_data.py` y agregamos lo siguiente:
```python
from ejemplo.models import Familiar
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")
```

Luego en la consola de visual estudio code vamos a ejecutar el script de la siguiente manera:

Esta oopción solo funciona en terminal bash:

```bash
python manage.py shell < seed_data.py
```

Para un terminal cmd o powershell, tienen que hacer, primero:
```cmd
python manage.py shell
```
una vez que estan en el shell hacer:

```python
import seed_data
```
al finalizar, para ambos casos, se tiene que ver un msj que diga: 
```
Se cargo con éxito los usuarios de pruebas
```

Despues volvemos a correr el servidor de pruebas y veremos una lista de familiares.

Siguientes pasos [clase_19_portfolio_django_mondelos_y_templates.md](clase_19_portfolio_django_mondelos_y_templates.md)

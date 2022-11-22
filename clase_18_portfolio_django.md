# Guía rapida de como correr un proyecto Django y versionarlo con github

- Crear un nuevo proyecto en github, una vez creado el proyecto obtener la url del repositorio origin y hacer en la terminal

 - ```git clone <reemplazar_con_tu_repo_url> .```

- ```django-admin startproject project .```

- ```python manage.py startapp ejemplo```

- ```python manage.py migrate```

- Crear la siguiente estructura de carpetas:
  ```ejemplo/templates/ejemplo```

- Dentro de la carpeta ```ejemplo/templates/ejemplo``` crear el archivo ```saludar.html``` y agregar el codigo 

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
    HOLA ESTO ES UN SALUDO DESDE UN TEMPLATE!!!!
</body>
</html>
```
  
- Abrir el archivo ```ejemplo/views.py``` y agregar el codigo

```python
from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html")
```

- Abrir el archivo ```project/settings.py``` y agregar la nueva app a la lista de
installed apps 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ejemplo.apps.EjemploConfig', # ESTA ES LA NUEVA APP !!
]
```

- Abrir el archivo ```project/urls.py``` y aregar la nueva ruta a la function saludar que esta en ```ejemplo/views.py```.

```python
from django.contrib import admin
from django.urls import path
from ejemplo.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
]
```
- Correr ```python manage.py runserver``` ir a [http://127.0.0.1:8000](http://127.0.0.1:8000)

- Para guardar los cambios en github:
  ```git add .```
  
  ```git commit -m "primer commit de mi proyecto"```
  
  ```git push origin main```

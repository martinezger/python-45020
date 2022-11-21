# Uso de Git
Todos los comandos que estan en este archivo tienen que ser ejecutados en una consola windows or bash.
- La consola bash se instala junto con GIT en windows.
- La consola bash en MacOS viene con el SO y solo tienen que buscar por TERMINAL en spotlight (cmd+espacio).

## Comandos de Configuración Git
Configurar el Nombre del usuario:
```bash
git config --global user.name "REEMPLAZAR CON TU NOMBRE Y APELLIDO"
```
Configurar el Email del usuario:
```bash
git config --global user.email "REEMPLAZAR CON TU CORREO ELECTRONICO QUE USAS EN GITHUB"
```
Verificar la configuración:

```bash
git config --list
```

## Comandos para Configurar un repositorio remoto
Configurar el repositorio creado en github:
```bash
git remote add origin NOMBRE_DE_REPO
```

## Comandos para crear un repositorio local Git:
Crear un repo con el nombre coder_house:
```bash
git init coder_house
```
esto les va a crear una carpeta con nombre coder_house.
Ahora entremos a la carpeta con el comando, change directory, cd :
```bash
cd coder_house
```
ahora para checkear que esta todo bien, corre el siguiente commando:
```bash
git status
```
Si lo hiciste bien tenes que ver un mensaje que dice `no commits yet`.

## Comandos para guardar un cambio local
Para guardar los cambios solo en nuestra pc.


Pasar el archivo a stagging:
```bash
git add ruta/del/archivo
```
Commitear:
```bash
git commit -m "UN MENSAJE DESCRIBIENDO EL CAMBIO"
```

## Comandos para guardar un cambio remoto
Ahora para poder tener el cambio en el repositorio remoto. Primero haga un commit local y luego.
```bash
git push origin main
```

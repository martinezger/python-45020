archivo_texto = open("chat.txt", "w")

contenido = """Claudio: Hola german como estas?
German: Todo bien, vos?.
Claudio: laksdjlakjsdlkajsd
German: alskdjlaksjdlkajsd
Ruben: laksjdlakjsdlkjas
"""

archivo_texto.write(contenido)
archivo_texto.close()


archivo_texto = open("chat.txt", "r")

linea_1 = archivo_texto.readline()
linea_2 = archivo_texto.readline()

print(linea_1)
print(linea_2)
archivo_texto.readline()

archivo_texto.close()


archivo_texto = open("chat.txt", "r")

for linea_de_texto in archivo_texto:
  print(linea_de_texto)

archivo_texto.close()

print("--------------------------------")

archivo_texto = open("chat.txt", "r")

contenido = archivo_texto.readlines()

for linea in contenido:
  print(linea)

archivo_texto.close()


print("--------------------------------")

archivo_texto = open("chat.txt", "r")

archivo_texto.seek(20)

for linea in archivo_texto:
  print(linea)

archivo_texto.close()

print("--------------------------------")


archivo_texto = open("chat.txt", "r")

archivo_texto.seek(20)

for linea in archivo_texto:
  print(linea[10:])

archivo_texto.close()

print("--------------------------------")


archivo_texto = open("chat.txt", "a")

contenido = "Claudio: Re bien!!\n"

archivo_texto.write(contenido)

archivo_texto.close()


archivo_texto = open("chat.txt", "r")

contenido = archivo_texto.readlines()

for linea in contenido:
  print(linea)

archivo_texto.close()
print("--------------------------------")

archivo_texto = open("chat.txt", "a")

contenido = "Romina: Re bien!!\n"

archivo_texto.write(contenido)

archivo_texto.close()


archivo_texto = open("chat.txt", "r")

contenido = archivo_texto.readlines()

for linea in contenido:
  print(linea)

archivo_texto.close()

print("--------------------------------")

archivo_texto = open("chat.txt", "r")
contenido = archivo_texto.readlines()
archivo_texto.close()

nuevo_contenido = []

for linea in contenido:
    nuevo_contenido.append(linea.replace("German", "Daniel"))
    print(linea)
    
archivo_texto = open("chat.txt", "w")
archivo_texto.writelines(nuevo_contenido)
archivo_texto.close()

archivo_texto = open("chat.txt", "r")

contenido = archivo_texto.readlines()

for linea in contenido:
  print(linea)
  
print("--------------------------------")


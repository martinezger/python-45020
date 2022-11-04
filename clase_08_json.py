import json
import csv

archivo_texto = open("contactos.json", "w")

contenido = """{

  "usuario_1": {
    "nombre": "German",
    "Apellido": "Martinez",
    "Telefonos": [
      "555-1234","555-9876"
    ]
  },

  "usuario_2": {
    "nombre": "German",
    "Apellido": "Martinez",
    "Telefonos": [
      "555-1234","555-9876"
    ]
  }

}"""

archivo_texto.write(contenido)
archivo_texto.close()


archivo_texto = open("contactos.json", "r")

contenido = archivo_texto.readlines()

for linea in contenido:
  print(linea)

archivo_texto.close()


print("----------------------------------")

archivo_texto = open("contactos.json", "r")

guia_telefonos = json.load(archivo_texto)

print(guia_telefonos)

archivo_texto.close()


guia_telefonos["usuario_1"]["nombre"] = "Federico"

archivo_texto = open("contactos.json", "w")

guia_telefonos_texto = json.dumps(guia_telefonos, indent=4)

archivo_texto.write(guia_telefonos_texto)

archivo_texto.close()

print("----------------------------------")

archivo_texto = open("contactos.csv", "w")

contenido = """usuario_1,german,martinez,555-1234
usuario_1,german,martinez,555-6789
usuario_2,Caro,Roldan,123123123
"""

archivo_texto.write(contenido)

archivo_texto.close()

print("-----------------DICT-----------------")

archivo_texto = open("contactos.csv", "r")
guia_telefonos = csv.reader(archivo_texto, delimiter=",")

print(guia_telefonos)

for numer_linea, linea in enumerate(guia_telefonos):
    print(f" {numer_linea + 1} {linea[0]} ---- {linea[1]}--- {linea[2]}")







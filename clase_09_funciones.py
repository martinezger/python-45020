def imprimir_por_pantalla_archivo_chat():
    print("------------INICIO---------------")
    archivo_texto = open("chat.txt", "r")
    for linea_de_texto in archivo_texto:
        print(linea_de_texto)
    archivo_texto.close() 
    print("------------FIN---------------")


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

imprimir_por_pantalla_archivo_chat()

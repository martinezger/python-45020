texto_entrada = "Hola Como estas, todo bien"
contador = 0

for palabra in  texto_entrada.split():
    if palabra.islower():
        contador += 1



print(texto_entrada)
print(f"La cantidad de lower es {contador}")


greet = 'hEllO woRLd'
"d".join(greet.split("d"))
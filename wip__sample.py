
import time
import random

'''
Genero una lista de 2000 elementos de tipo entero sin repetir.
[1, 2453, ... , 1980 ]
'''

lista_numeros = random.sample(range(10000), 2000)

'''
Genero un dictionario que tiene como llave los elementos de la lista de numeros
{ 1: "", 2453: "" ,..., 1980:"" }
A los efectos de probar la rapidez no nos interesa el valor en el dictionary por eso
se lo inicializa con ""
'''

dictionario_numeros = dict()
for numero in lista_numeros:
    dictionario_numeros[numero] = ""


# Se utiliza el último por que es el caso que tomaría mas tiempo en encontrar la lista.      
ultimo_elemento = lista_numeros[-1]
    
start_time = time.time()
lista_numeros.index(ultimo_elemento)
end_time = time.time()
tiempo_list = end_time - start_time

print(f"Para poder encontrar el {ultimo_elemento} en lista se tardo {(end_time - start_time)}")

start_time = time.time()
dictionario_numeros.get(ultimo_elemento)
end_time = time.time()
tiempo_dict = end_time - start_time
print(f"Para poder encontrar el {ultimo_elemento} en el dict se tardo {(end_time - start_time)}")


if tiempo_dict > tiempo_list:
    print(f"list es {tiempo_dict / tiempo_list} veces mas rápido")
else:
    print(f"dict es {tiempo_list / tiempo_dict} veces mas rápido")
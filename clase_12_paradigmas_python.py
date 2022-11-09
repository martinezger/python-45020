#Declarativa

import functools

una_lista = [1,2,3,4]
def sumar_func(x,y):
    return (x+y)

result = functools.reduce(sumar_func, una_lista)
print(result)

#imperativa

result = 0
for item in una_lista:
    result += item
print(result)

def sumar_proc(una_lista):
    resultado=0
    for item in una_lista:
        resultado += item
    return resultado

print(sumar_proc(una_lista))

#Orientada a objetos

class SumarLista:
    
    def __init__(self, una_lista):
        self.una_lista = una_lista
        self.resultado = 0
        
    def sumar(self):
        self.resultado=0
        for item in una_lista:
            self.resultado += item
        self.resultado

mi_sumador_de_listas = SumarLista(una_lista)
mi_sumador_de_listas.sumar()
print(mi_sumador_de_listas.resultado)
# suma de num pares
def suma_pares(a,b):
    
    if a % 2 == 0 and b % 2 == 0:
        return a + b
    
    return "a y b solo pueden ser pares"


assert suma_pares(1,2) == "a y b solo pueden ser pares"
assert suma_pares(2,2) == 4

PI = 3.14

def area_circunferencia(radio):
    c = PI * radio
    return c
    
a = [1,2,3,4,5,6]

def calcular_las_areas(lista_de_radios):
    for radio in lista_de_radios:
        print(area_circunferencia(radio))


"-1234".replace("-","").isnumeric()

'''
try:
    a = input("un numero")
    int(a)
    if a < 0:
        print("solo se aceptan num positivos")
except ValueError:
    print("Solo se aceptan valores enteros")
'''    


def separar(lista_entero):
    lista_entero.sort()
    lista_pares = []
    lista_impares = []
   
    for numero in lista_entero:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    return lista_impares, lista_pares


def test_separar_exito():
    assert separar([2,4,6,8,10]) == ([],[2,4,6,8,10])
    assert separar([1,3,5]) == ([1,3,5], [])
    assert separar([40,3,5,12]) == ([3, 5],[12, 40])
    assert separar([]) == ([],[])
    print("PASARON LOS TEST")
    

test_separar_exito()

print(separar([40,3,5,12]))



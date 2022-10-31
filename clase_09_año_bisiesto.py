def es_año_bisiesto(año):
    es_multiplo_de_cuatro = año % 4 == 0
    es_multiplo_de_cien = año % 100 == 0
    es_multiplo_de_cuatrocientos = año % 400 == 0
    es_biciesto = False
    
    if es_multiplo_de_cien and not es_multiplo_de_cuatrocientos:
        es_biciesto = False
    elif es_multiplo_de_cuatro:
        es_biciesto = True
        
    return es_biciesto
    
def test_de_año_biciesto():
    assert es_año_bisiesto(2012) == True
    assert es_año_bisiesto(2010) == False
    assert es_año_bisiesto(2000) == True
    assert es_año_bisiesto(1900) == False
    print("todos los test pasaron")




def una_func():
    global numero
    numero = 1


def otra_func():
    print(numero)
    
    
una_func()
otra_func()
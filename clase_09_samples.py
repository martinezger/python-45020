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
    

def test_es_año_bisiesto():
    assert es_año_bisiesto(2012) == True
    assert es_año_bisiesto(2010) == False
    assert es_año_bisiesto(2000) == True
    assert es_año_bisiesto(1900) == False
    
    
test_es_año_bisiesto()


def es_año_bisiesto_string(año):
    es_multiplo_de_cuatro = año % 4 == 0
    es_multiplo_de_cien = año % 100 == 0
    es_multiplo_de_cuatrocientos = año % 400 == 0
    es_biciesto = "no es bisiesto"
    
    if es_multiplo_de_cien and not es_multiplo_de_cuatrocientos:
        es_biciesto = "no es bisiesto"
    elif es_multiplo_de_cuatro:
        es_biciesto = "es bisiesto"
        
    return es_biciesto

def test_es_año_bisiesto_string():
    assert es_año_bisiesto_string(2012) == "es bisiesto"
    assert es_año_bisiesto_string(2010) == "no es bisiesto"
    assert es_año_bisiesto_string(2000) == "es bisiesto"
    assert es_año_bisiesto_string(1900) == "no es bisiesto"


if es_año_bisiesto(2000):
    print("febrero tiene 29 días")
else:
    print("febrero tiene 28 días")




def suma(*args, **kwargs):
    resultado = 0
    for arg in args:
        resultado += arg
        
    for value in kwargs.values():
        resultado += value
    
    return resultado
        

assert suma(1,2,3,4, a=1,b=2) == 13


def test_divi_error_cases():
    
    assert divi("a", 1) == "no se puede dividir"
    assert divi(1,"a") == "no se puede dividir"
    assert divi("a","b") == "no se puede dividir"
    assert divi(1,0) == "no se puede dividir"
    assert divi("","b") == "no se puede dividir"
    assert divi([], 1) == "no se puede dividir"
    
    print("pasaron todos los test de error")

def test_divi_success_cases():
    assert divi(1,1) == 1
    assert divi(1,-1) == -1
    
    print("pasaron todos los test de success")


a = 1

try:
   file = open("un_arch", "w")
    
except:
    print("oops algo salió mal")
else:
    print(f" la division")
finally:
    file.close()
    
    
    
def divi(a, b):
    if type(a) == str and a.isnumeric():
        a = int(a)
    if type(b) == str and b.isnumeric():
        b = int(b)
    if type(a) == int and type(b) == int:
        if b != 0:
            return a / b
    else:
        return"no se puede dividir"
    
    return "no se puede dividir"

test_divi_error_cases()
test_divi_success_cases()

def divi(a,b):
    
    try:
        return a / b
    except:
        return "no se puede dividir"
    

test_divi_error_cases()
test_divi_success_cases()


def divi(a,b):
    try:
        d
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        return "division por cero: b tiene que ser distinto de cero"
    except ValueError:
        a = 1
        def una():
            pass
        return "a y b solo pueden ser numeros enteros"
    except Exception as e:
        return f"alguna exception !!! no se que pasó {type(e).__name__}"


def divi(a,b):
    return a/b

try:
    divi(1,0)
except ZeroDivisionError:
    return "no se puede dividir"
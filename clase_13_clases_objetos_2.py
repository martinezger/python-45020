a = [1,2,3]
b = a.copy()

print(b)

b.pop()

f = 1

g = 1

h = 1

def print_persona(una_persona, un_numero_entero):
    if isinstance(una_persona, Persona):
        print(una_persona.calcular_edad())
    else:
        print("Solo se aceptan datos del tipo Persona")


class Persona:
  def __init__(self, nombre, apellido): # metodo constructor
    self.nombre = nombre
    self.apellido = apellido

  def print_uno_mismo(self):
    print(self)
    
persona_1 = Persona("German", "Martinez")  
persona_1.print_uno_mismo()
print(persona_1.nombre)

class Persona:
    idioma = "Castellano"
    
Persona.idioma = "Portuges"

class Persona:
  __idioma = "Castellano"
  
Persona.__idioma = "Portuges"
  


class Persona:
    
    def __init__(self, anio_nac):
        self.anio_nac = anio_nac
        
    @property    
    def edad(self):
        return 2022 - self.anio_nac 
        

una_persona = Persona(1987)

print(una_persona.edad)


class Persona:

  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
  
  def __eq__(self, otra_persona):
    return self.edad == otra_persona.edad

  def __gt__(self, otra_persona):
    return self.edad > otra_persona.edad

  def __lt__(self, otra_persona):
    return self.edad < otra_persona.edad
  
  def __str__(self):
    return(f"Nombre:{self.nombre}")
  



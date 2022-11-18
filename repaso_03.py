import sys

print(sys.argv)
print(f" {sys.argv[1]} + {sys.argv[2]} = { int(sys.argv[1]) + int(sys.argv[2])} ")


class Persona:
    def decir_hola(self):
        print("Hola")


persona_1 = Persona()

persona_1.decir_hola()


class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def presentarme(self, nombre_de_otro, *args, **kargs):
        print(f"Hola soy {self.nombre}, como estas {nombre_de_otro}")
    


persona_2 = Persona("german")
persona_2.presentarme("Federico")


class Usuario(Persona):

    numero_pi = 3.14

    def __init__(self, nombre, email, password):
        self.email = email
        self.password = password
        super().__init__(nombre)


    def info_user(self):
        print({self.email}, {self.password}, {self.nombre})



user1 = Usuario("germa", "ger@ger.com", "asd")

user1.presentarme("Federico")

user1.info_user()

from  repaso_03_paquete.repaso_03_modulo import Animal


animal_1 = Animal("chicho")

animal_1.saludar()


from repaso_03_paquete.repaso_03_modulo import Animal

animal_2 = Animal("chicha")

animal_2.saludar()

from repaso_03_paquete.repaso_03_modulo import sumar

sumar(3, 5)

from repaso_03_paquete.repaso_03_otro_modulo import Animal

animal_3 = Animal("perro")
animal_3.saludar()

from repaso_03_paquete.repaso_03_modulo import *

math.sqrt(25)

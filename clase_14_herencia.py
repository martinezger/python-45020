class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return f"{self.nombre} - ES PERSONA"
    
    def saludar(self):
        print("hola soy persona")
        
        
class ClienteBancario(Persona):
    def saludar(self):
        print("hola soy Cliente Bancario")


class GuardiaSeguridad(Persona):
    def saludar(self):
        print("hola soy Guardia de Seguridad")


class SuperPoderes:
    
    def saludar():
        print("hola soy un super heroe")
    
    def corre_rapido():
        pass
    
    def pelear():
        pass


class SuperHeroe(SuperPoderes, Persona):
    pass


class EmpleadoBancario(Persona):
    
    
    def __init__(self):
        self.mis_cliente = traer_clientes_de_la_base()
        
    
    def print_mis_cliente(self):
        for cliente in self.mis_clientes:
            print (cliente.nombre)
    
    
    def consultar_saldo_cliente(self, un_cliente):
        pass
    
    
    def __str__(self):
        return f"{self.nombre} - EMPLEADO DEL BANCO"
    

class Animal:
    
    def hablar(self):
        pass
    

class Perro(Animal):
    
    def hablar(self):
        print("Gua!!")


class Pato:

    def hablar(self):
        print("Cuak")

class Hormiga(Animal):
    
    def caminar(self):
        print("estoy caminando")

lista_de_animales = [Animal(), Perro(), Pato(), Hormiga()]

for animal in lista_de_animales:
    if hasattr(animal, "hablar"):
        animal.hablar()



class Vehiculo:
    
    def acelerar(self):
        pedalear_mas_rapido
    
    def frenar(self):
        presionar_freno
    
    def girar_izq(self):
        pass
    
    def girar_der(self):
        pass


class Triciclo(Vehiculo):
   
    def girar_izq(self):
        girar_manubrio_izq
    
    def girar_der(self):
        girar_manubrio_der


class Bicicleta(Triciclo):
    pass


class Automovil(Vehiculo):
    
    def acelerar(self):
        apretar_pedal_acelerador
    
    def frenar(self):
        presionar_pedal_freno
        
        
        






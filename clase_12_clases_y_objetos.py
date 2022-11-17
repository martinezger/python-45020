import math

class Punto:
    pass

punto_a = Punto()
punto_a.x = 1


punto_b = Punto()

def print_punto(un_punto):
    print("\tx\ty")
    print(f"\t{un_punto.x}\t{un_punto.y}")


class Recta:
    pass


class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def print_punto(self):
        print("\tx\ty")
        print(f"\t{self.x}\t{self.y}")
        
punto_a = Punto(1,2)
punto_a.print_punto()


punto_b = Punto(2,3)
punto_b.print_punto()


import math

class Punto():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Vector():
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
        
    def calcular_modulo(self):
        return math.sqrt((self.punto_b.x - self.punto_a.x)**2+(self.punto_b.y - self.punto_a.y)**2)

puntoA = Punto(1,2)
puntoB = Punto(2,4)

vector_1 = Vector(puntoA,puntoB)

print(vector_1.calcular_modulo())

Vector(Punto(2,3), Punto(3,4)).calcular_modulo()




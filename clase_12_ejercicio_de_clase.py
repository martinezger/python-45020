import math

class Punto():
    def __init__(self,x,y):
        self.x = x
        self.y = y

puntoA = Punto(1,2)
puntoB = Punto(2,4)



class Vector():
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
        
    def calcular_modulo(self):
        return math.sqrt((self.punto_b.x - self.punto_a.x)**2+(self.punto_b.y - self.punto_a.y)**2)
        

vector_1 = Vector(puntoA,puntoB)


print(vector_1.calcular_modulo())

Vector(Punto(2,3), Punto(3,4)).calcular_modulo()


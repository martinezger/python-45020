import math
import random


def func(a):
    a = math.sqrt(a)
    print(random(a))



class Animal:

    def __init__(self, nombre):
        self.nombre = nombre


    def saludar(self):
        print(f"HOla soy un animal con nombre {self.nombre}")


def sumar(a,b):
    print(a + b)


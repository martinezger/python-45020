#Expresiones Aritmeticas

2 + 3

#Expresiones Algebraicas

a= 1
a + 2

#Boolean/Boleano/Lógico/Binary/Binario
True
False

#Negacion
not True  # False
not False # True

# Comparadores Números
1 + 1 == 2 # True
1 + 1 == 3 # False

1 != 2 # True
2 != 2 # False

1 < 3  # True
3 <= 3 # True
4 < 1  # False
4 <= 1 # False

2 > 3  # True
3 >= 3 #True
5 > 8  # False
5 >= 8 #False

#Operadores String
"hola" == "hola" # True
"hola" == "hoLa" # False

# And
True and False # False
b = 1
a = 2
0 == (b * 0) and a == (33/33) and (5 == 1 + b ) # False

# Or
False or False == False
c = 1
c == 1 or c == 2 # True
c == 5 or c == 2 # False

#Not

not (True and False) # True
not (False or False) # True

not (True and False) == (not True or not False) # True

not(False or False) == (not False and not False) # True


# Expresiones anidadas

nombre = "German"
edad = 35

codicion_1 = "****" != nombre

codicion_2 = edad > 5 and edad < 20

codicion_3 = len(nombre) >= 4 and len(nombre) < 8

codicion_4 = edad * 3 > 35

print(codicion_1 and codicion_2 and codicion_3 and codicion_4)


# Operador de Asignación
d = 10
d += 1   # d = d + 1
d -= 1   # d = d - 1
d //= 2   # d = d / 2
d %= 2   # d = d % 2
d *= 2   # d = d * 2
d **= 2  # d = d ** 2

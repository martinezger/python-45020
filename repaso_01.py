print("## Cargar un dict mediante operador de asignación")
mi_dict = {}
print(mi_dict)
mi_dict["una_llave"] = "un valor"
print(mi_dict)
mi_dict["nombre"] = "German"
print(mi_dict)
mi_dict[1] = {"nombre": "Raul"}
print(mi_dict)

print("## verificar si la llave esta en el dict")
print(1 in mi_dict)
print("nombre" in mi_dict)
print("una_llave" in mi_dict)
print(33 in mi_dict)

print("## borrar una llave de dict")
print(mi_dict)
del mi_dict[1]
print(mi_dict)

print("Recorrer dos listas")

lista_num = [1,2,3,4]
lista_palabras = ["hola","chau", "adios", "pepe"]

for indice, elemento in enumerate(lista_num):
    print(lista_palabras[indice])
    print(elemento)
    

# Alta

while True:
    usuario = input("Ingrese usuario")
    nombre = input("nombre")
    edad = input("edad")
    
    if usuario in dict_user:
        print("Elija otro user")
        continue
    
    lista_info = [nombre, edad]
    
    dict_user[usuario] = lista_info 
    
    salir = input("Salir y/n")
    
    if salir == 'y':
        break


# Actualización
while True:
    usuario = input("Ingrese usuario")
    nombre = input("nombre")
    edad = input("edad")
    
    if usuario in dict_user:    
        lista_info = [nombre, edad]
        dict_user[usuario] = lista_info 
    else:
        print(f"No existe el usuario {usuario} en la base de datos")
        
    salir = input("Salir y/n")
    
    if salir == 'y':
        break

#Baja
    
while True:
    usuario = input("Ingrese usuario")
    if usuario in dict_user:    
       estoy_seguro = input("Salir y/n")
       if estoy_seguro:
        del dict_user[usuario]
        print(f"Se borro con éxito el usuario {usuario}")
    else:
        print(f"No existe el usuario {usuario} en la base de datos")
        
    salir = input("Salir y/n")
    
    if salir == 'y':
        break


for index, item in enumerate(('a', 'b', 4, '1', [])):
    print(f" index:{index} , value:{item}")


for item_a, item_b in zip(a,b):
    print(f"{item_a}, {item_b}")




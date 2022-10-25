colores= {"rojo":"red", "yellow":"amarillo"}
colores.items()

for color_español, color_ingles in colores.items():
  print(f"{color_español} -> {color_ingles}")
  
  
for valor in colores.values():
    print(valor)
    
for llave in colores.keys():
    print(llave)
    
    
lista_de_market = {"huevos":12, "cerveza": 120}
total = 0
for precio in lista_de_market.values():
    total += precio
    
print(f"total de la compra es {total}")

{
    1: {
        "nombre": "huevo",
        "stock":  1234,
        "precio": 120,
        },
    2: {
        "nombre": "coca-cola",
        "stock" : 12312,
        "precio": 320,
        }
}


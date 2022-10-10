# Checkear si es mayor de 18
edad = 18
if edad >= 18:
    print(f"{edad}, Es mayor de edad")


#Checkear si Es mayor de 18 y es Argentino
edad = 18
pais = "Arg"

if edad >= 18:
    print(f"{edad}, Es mayor de edad")

if pais == "Arg":
    print("Es extrajera")

    

#Checkear si es Argetino y si puede comprar Alcohol
edad = 17
pais = "Arg"

if edad >= 18:
  print("Es Mayor a 18.")
  if pais == "Arg":
    print("Puede comprar alcohol.")


#Checkar si Puede votar en Argentina

edad =  int(input("Ingrese edad:"))
pais  =  input("Ingrese país:") 
if pais == "Arg":
    if edad >= 16:
        print("Puede votar")

# se puede resumir en

edad = 16
pais = "Arg"

if edad >= 16 and pais == "Arg":
    print("Puede votar")


#Chekear si es alto
pais = "Arg"
if altura > "Arg": 
  print("Es Arg") ## True
else:  
  print("No es Arg") ## False


#Validar nota

if nota >= 9 :
  print("Sobresaliente")
elif nota >= 7 :
  print("BUeno")
else:
  print("Insuficiente")

#

nota = 9    
if nota >= 9 :
  print("Sobresaliente")
if nota >= 7 :
  print("Bueno")
else:
  print("Insuficiente")

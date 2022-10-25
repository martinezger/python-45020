'''
a = int(input("ingrese un número: "))
b = {1,2,3,}


print(f"El elemento {a} {'es' if a in b else 'no es'} parte del conjunto {b}.")
'''

a = 1
b = {1,2,4}

print('es' if a in b else 'no es')


set([1,2,3] + [1,2,3])
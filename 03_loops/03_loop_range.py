###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print("\nrange(): ")

# Generando una secuencia de números del 0 al 9

nums = range(10)
for num in nums:
    print(num)

# range(inicio,fin)
for num in range(5, 10):
    print(num)

# range(inicio, fin, paso)
for num in range(0, 100, 2):
    print(num)

for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

#para hacer lista
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# para hacerlo cinco veces
for _ in range(5):
    print("Hacer cinco veces algo")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
lista=[]
for num in range(1, 11):
    lista.append(num) 
print(lista)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
lista=[]
for num in range(1,21):
    if num %  2 != 0:
        lista.append(num)
print(lista)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
lista = []
for num in range(5,51):
    if num % 5 == 0:
        lista.append(num)
print(lista)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
lista = []
for num in range(10, 0, -1):
    lista.append(num)
print(lista)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0
for num in range(0,101):
    suma +=num
print(suma)
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numUsuario = int(input("Introduce un número: "))
for num in range(0,11):
    print(f"{numUsuario} X {num} = {numUsuario*num}")
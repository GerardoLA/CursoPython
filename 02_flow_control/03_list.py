###
# 03 - Listas
# Secuencias mutables de elementos. 
# Pueden contener cualquier tipo de dato.
###

# Crear una lista
import os
os.system("clear")

print("\n Crear una lista")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "uvas"] # lista de strings
lista3 = [1, "hola", 3.14159, True] # lista de tipos mixtos

lista_vacia = [] # lista vacía
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matriz

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a los elementos pr indice
print("\n Acceso a los elementos por índice")
print(lista2[0]) # manazanas
print(lista2[-1]) # uvas, indice negativo es desde el final

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]) Desde el inicio del 1 hasta el inicio del 4
print(lista1[:3]) # [1, 2, 3] Desde el inicio hasta el inicio del 3
print(lista1[3:]) # [4, 5] Desde el inicio del 3 hasta el final
print(lista1[:]) # [1, 2, 3, 4, 5] 

# HAY MÁS MAGIA
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(lista1[desde:hasta:paso]) # [2, 4] Desde el inicio del 1 hasta el inicio del 5, saltando de 2 en 2
print(lista1[::2]) # [1, 3, 5, 7, 9] Desde el inicio hasta el final, saltando de 2 en 2
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] Desde el final hasta el inicio

# Modificar una lista
lista1[0] = 20
print(lista1) # [20, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Añadir elementos a una lista
Lista1 = [1,  2, 3]

#forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1) # [1, 2, 3, 4, 5, 6]

#forma corta  y más eficiente
lista1 += [7, 8, 9]
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Recuperar la longitud de una lista
len(lista1) # 9
print("Longitud de la lista es: ", len(lista1))

######################################################

## Ejercicio 1 El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje secreto.
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print("\nEjercicio1: El mensaje secreto")
#mensaje_secreto = mensaje[7:]
print("".join(mensaje[7:]))

# Ejercicio 2 - Intercambio de posiciones
# Dada la siguiente lista:
# numeros  [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("\nEjercicio 2 - Intercambio de posiciones")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros [-1], numeros[0]
print(numeros)

# Ejercicio 3 - El sandwich de listas
# Dadas las siguientes listas:
# pan = ["pan de arriba"]
# ingredientes = ["lechuga", "tomate", "queso", "jamon"]
# pan_abajo = ["pan de abajo"]
# Crea una nueva lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("\nEjercicio 3 - El sandwich de listas")
pan = ["pan de arriba"]
ingredientes = ["Lechuga", "tomate", "queso", "huevo", "jamon"]
pan_abajo = ["pan de abajo"]
sandwich = print(pan + ingredientes + pan_abajo)

# Ejercicio 4 - Duplicando la lista
# Dada la siguiente lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
print("\nEjercicio 4 - Duplicando la lista")
lista = [1, 2, 3]
duplicada = print(lista * 2)

# Ejercicio 5 - Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento central, utilizando slicing.
print("\nEjercicio 5 - Extrayendo el centro")
lista = [1, 2, 3, 4, 5]
print("El elemento central es ",lista[len(lista)//2])

# Ejercicio 6 - REversa parcial
# Dada una lista, invierte solo la primeera mitad de la lista, utilizando slicing y concatenación.
# Ejemplo: lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
print("\nEjercicio 6 - Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista)//2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)

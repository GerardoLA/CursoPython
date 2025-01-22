###
# 03 - Listas
# Secuencias mutables de elementos. Pueden contener cualquier tipo de dato.
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
print(lista[:3]) # [1, 2, 3] Desde el inicio hasta el inicio del 3
print(lista[3:]) # [4, 5] Desde el inicio del 3 hasta el final
print(lista[:]) # [1, 2, 3, 4, 5] 

# HAY MÁS MAGIA
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[desde:hasta:paso]) # [2, 4] Desde el inicio del 1 hasta el inicio del 5, saltando de 2 en 2
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


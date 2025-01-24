###
# 04 - Listas Metodos
# Los metodos mas importantes de las listas
###

import os
os.system("clear")

lista = ["a", "b", "c", "d", "e"]

# Añadir o insertar elementos a la lista

lista.append('j') # añade un elemento al final de la lista
print(lista) # [a, b, c, d, e, j]

lista.insert(1, '@') # inserta un elemento en la posicion que le indiques
print(lista) # [a, @, b, c, d, e, j]

lista.extend([1, 2, 3]) # añade varios elementos al final de la lista
print(lista) # [a, @, b, c, d, e, j, 1, 2, 3]

# eliminar elementos de la lista
lista.remove('@') # elimina el primer elemento que coincida con el valor, la primera @

ultimo_elemento = lista.pop() # elimina el último elemento de la lista y lo devuelve
print(ultimo_elemento) # 3

lista.pop(1) # elimina el elemento en la posición que le indiques, es el indice, el elemnto que este en la posición 1
print(lista) # [a, b, c, d, e, j, 1, 2]

#eliminar por lo bestia
del lista[0] # elimina el elemento en la posición que le indiques, es el indice, el elemnto que este en la posición 0

lista.clear() # elimina todos los elementos de la lista

# Eliminar un rango de elementos
del lista[1:3] # elimina los elementos en el rango que le indiques, del principio del 1 al principo del 3
print(lista) # [a, d, e, j, 1, 2]

# Más métodos útiles
print('Ordenar listas modificando la lista original')
numbers = [3, 10, 45, 1, 2, 8]
numbers.sort() # ordena los elementos de la lista
print(numbers) # [1, 2, 3, 8, 10, 45]

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 45, 1, 2, 8]
sorted_numbers = sorted(numbers) # crea una nueva lista ordenada
print(sorted_numbers) # [1, 2, 3, 8, 10, 45]

print('Ordear una lista de cadenas de texto todo minúsculas')
frutas = ['naranja', 'manzana', 'fresa', 'pera']
sorted_frutas = sorted(frutas) # ordena las cadenas de texto
print(sorted_frutas) # ['fresa', 'manzana', 'naranja', 'pera']

print('Ordenar una lista de cadenas de texto mezcladas mayúsculas y minúsculas')
frutas = ['Naranja', 'manzana', 'Fresa', 'pera']
frutas.sort(key=str.lower) # ordena las cadenas de texto ignorando mayúsculas y minúsculas      
print(frutas) # ['Fresa', 'manzana', 'Naranja', 'pera']     

# Más cositas utiles
animals = ['gato', 'perro', 'mono', 'elefante', 'gato']
print(len(animals)) # tamaño de la lista -> 5
print(animals.count('gato')) # cuantas veces aparece un elemento en la lista -> 2
print('gato' in animals) # Comprueba si hay un 'gato' en la lista -> True
print('raton' in animals) # Comprueba si hay un 'raton' en la lista -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido.
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 15.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

print("\nEjercicio 1: Añadir y modificar elementos")
lista = list(range(1,16))
print(lista)
lista.append(6)
print(lista)
lista.insert(2,10)
print(lista)
lista[0]= 0
print(lista)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en la lista_a usando remove()
# Elimina el elemento en el indice 3 de la lista_a usando pop(). Imprime el eliminado.
# Limpia completamente lista_b usando clear().

print("\nEjercicio 2 Combina y limpiar las listas")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
eliminado = lista_a.pop(3)
print("El elemento eliminado es: ",eliminado)
lista_b.clear()
print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print("\nEjercicio 3: Slicing y eliminación con del")
numeros = list(range(1,11))
del numeros[2:5]
print(numeros)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuantas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

print("\nEjercicio 4: Ordenar y contar")
numeros = [5, 2, 8, 1, 9, 4, 2]
numeros.sort()
print(numeros)
print("El número 2 aparece ", numeros.count(2), "veces en la lista")
if 7 in numeros:
    print("El 7 si está en la lista")
else:
    print("7 no está en la lista.")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números[1, 2, 3]
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro lista(original, copia_1, copia_2, referencia) y observa los cambios.

print("\nEjercicio 5: Copia vs. referencia")
original = [1, 2, 3]
copia_1 = original[:]
print("La lista original es: ",original)
print("La copia_1 es: ",copia_1)
copia_2 = original.copy()
print("La copia_2 hecha con copy() es: ",copia_2)
referencia = original
print("Referencia es: ",referencia)
referencia[0]=10
print("Referencia modificaodo es:",referencia)

print(f"Original es: {original}")
print(f"copia_1 es: {copia_1}")
print(f"copia_2 es: {copia_2}")
print(f"Referencia es: {referencia}")

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "Banana", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

print("\nEjercicio 6")
lista = ["Manzana", "pera", "Banana", "naranja"]
lista.sort(key=str.lower)
print(lista)
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

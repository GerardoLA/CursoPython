###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mienttras itera un iterable o una lista
###

print("\ Bucle for: ")

# Iterar una lista

# frutas = ["manzana", "pera", "mandarina"]
# for fruta in frutas:
#     print(fruta)

# Iterar  sobre cualquier cosa iterable

# cadena = "midudev"
# for caracter in cadena:
#     print(caracter)

# enumerate() permite iterar sobre los elementos y saber el index y los elementos
# frutas = ["manzana", "pera", "mandarina"]
# for index, value in enumerate(frutas):
#     print(f"El indice es {index} y la fruta es {value}")

# Bucles anidados
# letras = ["a", "b", "c"]
# numeros = [1, 2, 3]

# for letra in letras:
#     for numero in numeros:
#         print(f"{letra}{numero}")

# break
# animales = ["perro", "gato", "loro", "raton", "loro", "pez", "canario"]
# for idx,animal in enumerate(animales):
#     print(animal)
#     if animal == "loro":
#         print(f"El loro esta escondido en el indice{idx}")
#         break

#continue
# print("\n continue: ")
# animales = ["perro", "gato", "loro", "raton", "loro", "pez", "canario"]
# for idx,animal in enumerate(animales):
#     print(animal)
#     if animal == "loro":
#         continue
#         print(animal)

# Comprensión de listas (list comprehension)
# animales = ["perro", "gato", "loro", "raton", "loro", "pez", "canario"]
# animales_mayus = [animal.upper() for animal in animales]
# print(animales_mayus)

# Muestra los números pares de una lista
# pares = [num for num in [1, 2, 3, 4 , 5, 6, 7, 8] if num % 2 == 0]
# print (pares)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
pares = [num for num in range(2,20)if num % 2 == 0]
print (pares)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
media = suma/len(numeros)
print(f"La media es {media}")
        

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 10]
mayor = 0
for num in numeros:
    if num > mayor:
        mayor = num
print(f"El número mayor es {mayor}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
listaLargas = [palabra for palabra in palabras if len(palabra) > 5]
print (listaLargas)
    


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"] 
inicial = input("Introduce una letra: ").lower()
contador = 0
for palabra in palabras:
    if palabra.lower().startswith(inicial):
        contador += 1
print(f"Hay {contador} palabras que empiezan por {inicial}")      
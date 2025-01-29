###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mienttras itera un iterable o una lista
###

print("\ Bucle for: ")

# Iterar una lista

frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# Iterar  sobre cualquier cosa iterable

cadena = "midudev"
for caracter in cadena:
    print(caracter)

# enumerate() permite iterar sobre los elementos y saber el index y los elementos
frutas = ["manzana", "pera", "mandarina"]
for index, value in enumerate(frutas):
    print(f"El indice es {index} y la fruta es {value}")

# Bucles anidados
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
animales = ["perro", "gato", "loro", "raton", "loro", "pez", "canario"]
for idx,animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice{idx}")
        break

#continue
print("\n continue: ")
animales = ["perro", "gato", "loro", "raton", "loro", "pez", "canario"]
for idx,animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        continue
        print(animal)

# Comprensión de listas (list comprehension)
animales = ["perro", "gato", "loro", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4 , 5, 6, 7, 8] if num % 2 == 0]
print (pares)
        
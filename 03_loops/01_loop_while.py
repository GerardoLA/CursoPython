###
# 01 -Bucles (while)
# Permiten ejecutar un bloque de códgo repetidamente mientras se cumpla la condición
###
print("\nBucle while:")
#Bucle con una simple condición
contador = 0
while contador <=5:
    print (contador)
    contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\nBucle con break")

contador = 0
while True:
    print(contador)
    contador += 1
    if contador==5:
        break #sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y contiinuar ocn el bucle
print("\nBucle continue")
contador = 0
while contador < 10:
    contador +=1
    if contador % 2 == 0:
        continue
    # es continua haciendo el bucle y no hace l siguiente paso, que seria el print
    print(contador)

# else, está condición cuando se ejecuta?
print("\nbucle while con else")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

# pedirle al usuario un número que tiene que ser positivo, si no, no le dejamo en paz
print("\n")
""" numero =  -1
while numero < 0:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
        print("El número debe ser positivo. intenta otra vez")

print(f"El númeroi que has introducido es {numero}") """

numero =  -1
while numero < 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:
            print("El número debe ser positivo. intenta otra vez")
    except:
        print("Lo que debes introducir es un número, si no falla")

print(f"El númeroi que has introducido es {numero}")

###
# 01 -Bucles (while)
# Permiten ejecutar un bloque de códgo repetidamente mientras se cumpla la condición
###

# print("\nBucle while:")

# #Bucle con una simple condición
# contador = 0

# while contador <=5:
#     print (contador)
#     contador += 1 # es super importante para evitar un bucle infinito

# # utilizando la palabra break, para romper el bucle
# print("\nBucle con break")

# contador = 0
# while True:
#     print(contador)
#     contador += 1
#     if contador==5:
#         break #sale del bucle

# # continue, que lo hace es saltar esa iteración en concreto
# # y contiinuar ocn el bucle
# print("\nBucle continue")
# contador = 0
# while contador < 10:
#     contador +=1
#     if contador % 2 == 0:
#         continue
#     # es continua haciendo el bucle y no hace l siguiente paso, que seria el print
#     print(contador)

# # else, está condición cuando se ejecuta?
# print("\nbucle while con else")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
# else:
#     print("El bucle ha terminado")
    

# # pedirle al usuario un número que tiene que ser positivo, si no, no le dejamo en paz
# print("\n")
# """ numero =  -1
# while numero < 0:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0:
#         print("El número debe ser positivo. intenta otra vez")

# print(f"El númeroi que has introducido es {numero}") """

# numero =  -1
# while numero < 0:
#     try:
#         numero = int(input("Escribe un número positivo: "))
#         if numero < 0:
#             print("El número debe ser positivo. intenta otra vez")
#     except:
#         print("Lo que debes introducir es un número, si no falla")

# print(f"El númeroi que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")
numero = 11
while numero  > 1:
    numero -= 1
    print (numero)

# # Ejercicio 2: Suma de números pares (while)
# # Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")
num = 0
while num < 20:
    num +=1
    if num % 2 == 0:
        print(num)  
# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nEjercicio 3:")
num = int(input("introduce un numero: "))
num_original = num
print("X",num)
factorial = 1
while num > 1:
    factorial *= num
    num -= 1 
    print("X",num)     
print("------")
print(factorial,f"--> El factorial de {num_original} es {factorial}")



# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

password = ""

while len(password) < 8:
    password = input("Introduce una contraseina de al menos 8 caracteres: ")
    if len(password) < 8:
        print(f"Try again, tiene que ser al menos de 8, has metido {len( password)}!!")
print("Ok! Password correcto")



# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")
numero = int(input("Introduce un número del 1 al 10: "))
contador = 0
while contador < 10:
    contador += 1
    print(f"{numero} X {contador} = {numero*contador}")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

num = int(input("Introduce un número: "))
for num in range(2,num):
    if num > 1:
        cont=0
        i=2
        while i<num and cont==0:
            resto=num%i
            if resto == 0:
                cont += 1
            i+=1
        if cont ==0:
            print(num)



    
    
    

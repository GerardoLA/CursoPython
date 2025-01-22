# 01 - Sentencias condicionales (if, elif, else)
# Permiter ejecutar un bloque de código si se cumple ciertas condiciones.
###

import os
os.system("clear")

print("\n Sentencia simple coondicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")  ## ojo la tabulación en python es muy importante, si no cumples las tabulaciones funcionaría sin cumplir la condición


print("\n Sentencia condicional con else")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:   
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 7
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Suspendido!!")

print("\n condiciones múltiples")
edad = 25
tiene_carnet = False

if edad >= 19 and tiene_carnet:
    print("Puedes conducir")
else:
    print("Policia!!")

# un pueblo de Isla Margarita
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en Isla Margarita")
else:
    print("Paga la mordida y puedes conducir")

es_fin_de_semana = False
# en javaScript -> !
if not es_fin_de_semana:
    print("A trabajar!!")

print("\n anidar condiciones")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes entrar a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la discoteca")
 # Más fácil
if edad < 18:
    print("No puedes entrar a la discoteca")
elif tiene_dinero:
    print("Puedes entrar a la discoteca")
else:
    print("Quedate en casa")

numero = 5
if numero:
    print("El número es distinto de cero")
numero = 0
if numero: #false
    print("aquí no entrará nunca")

nombre = ""
if nombre:
    print("El nombre no es vacío")

numero = 5
es_el_cinco = numero == 5 # comparación
if es_el_cinco:
    print("El número es cinco")

print("\n La condición ternaria")
# Es una forma concisa de escribir una sentencia if else
# [códio si cumple la condición] if [condición] else [código si no cumple la condición]

edad = 17
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

############################################
# Ejercicios
############################################

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál de los dos es mayor o si son iguales.

""" numero1 , numero2 = input("Introduce dos números separados por un espacio: ").split()
numero1, numero2 = int(numero1), int(numero2)
if numero1 == numero2:
    print("Los números son iguales")
elif numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
else:
    print(f"{numero2} es mayor que {numero1}") """

numero1 = input("Introduce el primer número: ")
numero1 = float(numero1)
numero2 = input("Introduce el segundo número: ")
numero2 = float(numero2)

if numero1 == numero2:
    print("los números son iguales")
elif numero1 < numero2:
    print(f"{numero2} es mayor que {numero1}")
else:
    print(f"{numero2} es mayor que {numero1}")

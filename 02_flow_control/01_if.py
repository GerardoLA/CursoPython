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
print("\nEjercicio 1: Determinar el mayor de dos números")
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

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado.
print("\nEjercicio 2: Calculadora simple")
numero1 = input("introduce el primer número:")
numero1 = float(numero1)
numero2 = input("introduce el segundo número:")
numero2 = float(numero2)
operacion = input("introduce el signo de la operacion, '+' si quieres sumar, '-' si quieres restar, '*' si quieres multiplicar y '/' si quieres dividir: ")
if operacion == "/" and numero2 == 0:
    print("No se puede dividir por cero")
elif operacion == "+":
    print ("resultado = ",numero1 + numero2)
elif operacion == "-":
    print ("El resutado de la resta es: ",numero1 - numero2)
elif operacion == "*":
    print("El resultdo de la multiplicaión es: ",numero1 * numero2)
elif operacion == "/":
    print("El resultado de la division es: ",numero1 / numero2)
else:
    print("Operación no valida")

# Ejercicio 3 : Año bisiesto
# Pide al usuario que introduzca un año y determine si es bisiesto o no.
# Un año es bisiesto si es múltiplo de 4, excepto si es divisible por 100 pero no por 400.
print("/nEjercicio 3: Año bisiesto")
año = int(input("Introduce un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 ==0):
    print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto") 

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 en adelante)
print("\nEjercicio 4: Categorizar edades")
edad = int(input("Introduce una edad valida: "))
if edad >= 0 and edad < 3:
    print("Bebé")
elif edad >= 3 and edad < 13:
    print("Niño")
elif edad >= 13 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 65:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no valida")
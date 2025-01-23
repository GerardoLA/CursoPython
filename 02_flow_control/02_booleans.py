###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

import os
os.system("clear")

# Los booleanos representan valoes de verdad;  True o False

print("\n Valores Booleanos básicos:")
print(True)
print(False)

# Operadores de comparación : devuelven un valor booleano
print("\n Operadores de comparación")
print("5 ==5",5 == 5)  # True
print("5 == 6",5 == 6)  # False
print("5 != 6",5 != 6)  # True
print("5 != 5",5 != 5)  # False
print("5 > 5",5 > 5)  # False
print("5 >= 5",5 >= 5)  # True
print("5 < 5",5 < 5)  # False


print("\n Comparación de cadenas")
print("'manzana' < 'pera':", 'manzana' < 'pera') # True
print("'Hola' == 'hola':", 'Hola' == 'hola') # False

# Operadores lógicos: and, or, not
print("\n Operadores lógicos")
print("True and True:",True and True)    # True
print("True and False:",True and False)  # False
print("True or False:",True or False)    # True
print("False or False:",False or False)  # False
print("not True:",not True)              # False
print("not False:",not False)            # True

# Tablas de verdad
print("\n Tablas de verdad")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)


print("\La condición ternaria")
# Es una forma concisa de escribir una sentencia if else
# [códio si cumple la condición] if [condición] else [código si no cumple la condición]

edad = 17
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)
# Operadores de comparación : devuelven un valor booleano
print(5 == 5)  # True
print(5 == 6)  # False
print(5 != 6)  # True
print(5 != 5)  # False
print(5 > 5)  # False
print(5 >= 5)  # True
print(5 < 5)  # False


print("\n Comparación de cadenas")
print("Python" == "Python")  # True
print("Python" == "python")  # False
print("Python" != "python")  # True
print("Python" != "Python")  # False
print("Python" > "Java")  # True
print("Python" < "Java")  # False
print("Python" >= "Java")  # True
print("Python" <= "Java")  # False


# Tablas de verdad
print("\n Tablas de verdad")
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False


print("\La condición ternaria")
# Es una forma concisa de escribir una sentencia if else
# [códio si cumple la condición] if [condición] else [código si no cumple la condición]

edad = 17
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)
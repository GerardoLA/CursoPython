##
# 04 - Variables
# Las variables son contenedores de datos que se utilizan para almacenar información.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.

# Asignar una variable  
# solo hace falta pooner esto
my_name = "GerTato"
print(my_name)

age = 32
print(age)

age =50
print(age)

# tipado dinámico: el tipo de dato se determine en tiempo de ejecución
# que no tienes que declararlo esplicitamente
name = "Gerardo"
print(type(name))

name = 10
print(type(name))

# tipado fuerte: Python no realiza conversiones de tipo automáticas.
# print(10 + "2") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# f-string (literal de cadeba de formato)
# desde python 3.6
print(f"Hola {my_name}, tengo {age - 5} años")

# No recomendada forma de asignar variables
name, age, city = "Gerardo", 32, "Madrid" # Funciona pero no es recomendable

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" # Snake case
nombre = "ok" # Camel case

miNombreDeVariable = "no-recomendado" # Camel case
MiNombreDeVariable = "no-recomendado" # Pascal case
minombredevariable = "no-recomendado" # Lower case

mi_nombre_de_variable_123 = "ok" 

MI_CONSTANTE = 3.14 # UPPER_CASE -> Constantes NO EXISTEN como tal , pero se usa esta convención.

# nombres no validos de variables
# 123_mi_variable = "no" # SyntaxError: invalid syntax
# mi-variable = "no" # SyntaxError: can't assign to operator
# mi variable = "no" # SyntaxError: invalid syntax

# True = False # SyntaxError: can't assign to keyword

# Palabras reservadas
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

is_user_looged_in:bool = True
print(is_user_looged_in)

name:str = "GerTato"
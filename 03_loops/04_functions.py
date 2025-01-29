###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

""" Definición de una función

def nombre_de_la_funcion(parametro, parametro2, ...):
    #docstring
    #cuerpo de la funcion
    return valor_de_retorno # opcional

"""

# ejemplo de una funcion para imprimir algo en consola
def saludar():
    print("hola")
saludar()

# Ejemplo de una función con parámetro
def saludar_a(nombre):
    print(f"!Hola {nombre}!")

saludar_a("midudev")
saludar_a("Tato")

# Funciones con más parametros
def sumar(a, b):
    suma = a+ b
    return suma
result = sumar(2, 3)
print(result)

# Documenatar las funciones con docstring
def restar(a, b):
    """ Resta dos números y devuelve el resultado """
    return a - b

# parámetros por defecto
def multiplicar(a, b = 2):
    return a * b
print(multiplicar(2))

# Argumentos por clase
def describir_por_persona(nombre, edad, sexo):
    print(f"soy {nombre}, tengo {edad} años y me identifico como {sexo}")
# parametros porposición
describir_por_persona("Tato", 50, "chimpance")

# Argumentos por clave
# parámetros nombrados
describir_por_persona(sexo="mono", nombre="Tato", edad = 50)

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma
print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8 , 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad = 120, sexo= "gato")
print("\n")
mostrar_informacion_de(nombre = "Igor", edad = 50, country = "Bask_country")
print("\n")
mostrar_informacion_de(nombre = "Teit", equipo = "Real sociedad", es_sub = False, is_rich = False)
print("\n")
mostrar_informacion_de(nombre = "Arkonada", nickname = "God", position = "goalkeper")


# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora
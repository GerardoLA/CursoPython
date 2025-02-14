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
# def saludar():
#     print("hola")
# saludar()

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#     print(f"!Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("Tato")

# # Funciones con más parametros
# def sumar(a, b):
#     suma = a+ b
#     return suma
# result = sumar(2, 3)
# print(result)

# # Documenatar las funciones con docstring
# def restar(a, b):
#     """ Resta dos números y devuelve el resultado """
#     return a - b

# # parámetros por defecto
# def multiplicar(a, b = 2):
#     return a * b
# print(multiplicar(2))

# # Argumentos por clase
# def describir_por_persona(nombre, edad, sexo):
#     print(f"soy {nombre}, tengo {edad} años y me identifico como {sexo}")
# # parametros porposición
# describir_por_persona("Tato", 50, "chimpance")

# # Argumentos por clave
# # parámetros nombrados
# describir_por_persona(sexo="mono", nombre="Tato", edad = 50)

# # Argumentos de longitud de variable (*args):
# def sumar_numeros(*args):
#     suma = 0
#     for num in args:
#         suma += num
#     return suma
# print(sumar_numeros(1, 2, 3, 4, 5))
# print(sumar_numeros(1, 2))
# print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8 , 9, 10))

# # Argumentos de clave-valor variable (**kwargs):
# def mostrar_informacion_de(**kwargs):
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# mostrar_informacion_de(nombre="midudev", edad = 120, sexo= "gato")
# print("\n")
# mostrar_informacion_de(nombre = "Igor", edad = 50, country = "Bask_country")
# print("\n")
# mostrar_informacion_de(nombre = "Teit", equipo = "Real sociedad", es_sub = False, is_rich = False)
# print("\n")
# mostrar_informacion_de(nombre = "Arkonada", nickname = "God", position = "goalkeper")


# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

# Ejercicio 1: Imprime los números del 10 al 1 usando while (modifico para que sea el que el usuario introduzca)
# def imprimir_cuenta_atras():
#     """Imprime la cuenta atrás desde el número que introduzca el usuario hasta el 1"""
#     numero = int(input("introduce  un número: "))
#     print(numero)
#     while numero > 1:
#         numero -= 1
#         print (numero) 
# imprimir_cuenta_atras()  

# # Ejercicio 2: Suma de números pares, usando while, de los números que haya desde el 1 al número que introduzca el usuario
# def suma_pares():
#     """Suma de números pares, desde el 0 hasta el número introducido por el usuario"""
#     numero = int(input("introduce un número: "))
#     num = 0
#     suma = 0
#     while(num < numero):
#         num += 1
#         if num % 2 == 0:
#             suma += num
#     print(suma)
# suma_pares()

# # Ejercicio 3: Factorial de un número , usando while, de un número positivo introducido por el usuario
# def factorial():
#     """Calcula el factorial del número que introduzca el usuario"""
#     num = int(input("introduce un número: "))
#     print(f"  {num}")
#     fact = 1    
#     while num > 1:
#         fact *= num 
#         num -= 1
#         print("X",num)
#     print("-------")
#     print(fact)
#     print(f"El factorial de {num} es {fact}")
# factorial()

# # Ejercicio 4 = Validación de contraseña
# def valida_password():
#     """Valida que el password introducido sea al menos de 8 caracteres"""
#     while len(input("Introduce tu password: ")) < 8:
#         print("El password debr ser de al menos 8 caracteres")
#     print("ok")
# valida_password()

# Ejercicio 5 Tabla de multiplicar
# print("\nEjercicio5")
# def tabla_multiplicar():
#     """Hace la tabla del número que introduzca el usuario"""
#     num =int(input(f"Introduce un numero del 1 al 10: "))
#     while num <1 or num > 10:
#         num =int(input(f"Introduce un numero del 1 al 10: "))
#     i=10
#     while i >= 0:
#         print(f"{num} X {i} = {num*i}")
#         i -= 1
            
# tabla_multiplicar()

# # Ejercicio 6
# print("\nEjercicio6") 
# def numeros_primos():
#     """Muestra los numeros primos menores del que introduzca el usuario"""
#     num = int(input("Introduce un número: "))
#     for num in range(2,num):
#         if num > 1:
#             cont=0
#             i=2
#             while i<num and cont==0:
#                 resto=num%i
#                 if resto == 0:
#                     cont += 1
#                 i+=1
#             if cont ==0:
#                 print(num)

# numeros_primos()

# # Ejercicio 7 
# print("\nEjercicio7")
# def numeros_pares():
#     """Muestra los numeros pares menores del que introduzca el usuario"""
#     pares = [num for num in range(2,int(input("introduce un numero: ")))if num % 2 == 0]
#     print(pares)

# numeros_pares()

# print("\nFunción 8 del ejercicio 2 for") 
# def media():
#     array = []
#     print("Introduce los números uno a uno. Presiona Enter sin introducir nada para terminar:")

#     while True:
#         entrada = input("Introduce un número: ")
#         if entrada == "":
#             break
#         try:
#             num = int(entrada)
#             array.append(num)
#         except ValueError:
#             print("Por favor introduce un número válido.")
    
#     if not array:
#         print("No se introdujeron números.")
#         return

#     print(f"El array resultante es {array}")
    
#     suma = 0
#     for num in array:
#         suma += num
#     media = suma / len(array)
#     print(f"La media de {array} es {media}")

# media()

print("\nFunción 9 ejercicio 3 for")
def maximo(lista):
    """Encontrar el número mayor de una lista dada"""
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    print(f"El número mayor es {mayor}") 

maximo([90, 45, 10, 44, 127, 38, 9, 91, 4])

print("\nFunción 10 -  Ejercicio 4 for")
def cadenaLong(cadena):
    """Filtra cadena porlonfitug mayor de 5"""
    cadena2=[]
    for pal in cadena:
        if len(pal) > 5:
            cadena2.append(pal)
    print(cadena2)
cadenaLong(["ksdjhfkj", "arrai", "hondarbi", "sdf", "goazenMaink", "uno", "bi"])

print("\nFunción 11 del Ejercicio 4 for")
def contPalabras(palabras):
    letra = input("Introduce una letra: ").lower()
    contador = 0
    for palabra in palabras:
        if palabra.lower().startswith(letra):
            contador += 1
    print(f"Hay {contador} palabras que empiecen por {letra}")

  
contPalabras(["house", "tree", "sun", "Macallan","elephant", "moon", "car"])




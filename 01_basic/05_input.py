###
# 05 - Entrada de usuario (input()) -  Versión simplificada
# La función input() nos permite obtener datos del usuario a través de la consola.
###

nombre = input("¿Cómo te llamas?\n") 
print(f"¡Hola {nombre}, encantado de conocerte!")

age = input("¿Cuántos años tienes?\n")
age = int(age)
print(type(age))
print(f"¡Vaya, {nombre}! ¡No pareces de {age} años!")

print("Obtener multiples valores a la vez")
country, city = input("¿De qué país y ciudad eres?\n").split()
print(f"Vives en {city}, {country}!")
##
# 01 -  Expresiones regulares
#


"""Las expresiones regulares son una secuencia de caracterese que forman un patrón de busqueda
    Se utilizan para la busqueda de cadenas de texto, validación de datos, etc."""

""" Por qué aprender Regex

- Buesqueda avanzada: Enconrar patrones especificos en textos grandes de forma rápid y precisa. (Un editor de
MArkdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email , teéfono, etc son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar paretes de la cadena de texto fácilmente
"""

# importar el móudlo de expresiones eregulares "re"
import re
pattern = "Hola"
text= "Hola mundo"

result = re.search(pattern, text)

if result:
    print("He encontrado el patrón del texto")
else:
    print("Mo he encontrado el patrón del texto")


# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start()
print(result.start())

# .end()
print(result.end())

# EJERCICIO 01
# 
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Perdo solo hacefalta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)
print(f"He encontrado el patrón de texto en la posicion {found_ia.start()} y termina en la posición {found_ia.end()}")

# Encontrar todas las coincidencias de un patrón 
 # .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. aunque Python nos estan difícil, ojo con Python"
pattern = "Python"
matches = re.findall(pattern, text)
if matches:print(matches)

# EJERCICIO Encuentra todas las ocurrencias


# Reemplazar el texto
# .sub()
text =  "Hola mundo! Hola de nuevo"
pattern = "Hola"
replacement = "Adios"
new_text = re.sub(pattern, replacement, text, count=1, flags=re.IGNORECASE)
print(new_text)

#
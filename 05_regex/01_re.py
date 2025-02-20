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

# 1. mportar el móudlo de expresiones eregulares "re"
import re
# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
# 3. El texto donde queremos buscar
text= "Hola mundo"
# 4. Usar la función de busqueda "re"
result = re.search(pattern, text)

if result:
    print("He encontrado el patrón del texto")
else:
    print("No he encontrado el patrón del texto")


# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(result.start())

# .end() devolver la posición final de la coincidencia
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto e indica en que posición empieza y termina la coincidencia
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
    print(f"He encontrado el patrón de texto en la posicion {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
    print("No he encontrado el patrón de texto")
# Encontrar todas las coincidencias de un patrón 
 # .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. aunque Python nos estan difícil, ojo con Python"
pattern = "Python"
matches = re.findall(pattern, text)
print(len(matches))

# ----------------------------
 # iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gustas Python, Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza 
# y termina cada coincidencia y cuantas veces se encontro,
text = "Este es el curso de Python de midudev. !Suscribete a midudev si te gusta este contendido midu "
pattern = "midu"
matches = re.findall(pattern, text)
print(f"El número de ocurrencias '{pattern} son: {len(matches)}")
matches = re.finditer(pattern,text)
for match in matches:
    print(match.group(),match.start(),match.end())

### Modificadores
# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento
# re.IGNORACASE: Ignora las mayúsculas y minúsculas
text = "Todo el mundo  dice que la IA va a quitar trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found:
    print(found)
    print(f"Encontrada {len(found)} veces")

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "Python" en el siguiente texto, sin distinguir entre mayúsculas y minúsciulas
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "Python"
found = re.findall(pattern, text, re.IGNORECASE)

if found:
    print(f"Se ha encontrado {len(found)} veces")
    print(found)

# Reemplazar el texto
# .sub() reemplaza todas las coincidencias de un patrón en un texto
text =  "Hola mundo! Hola de nuevo. Hola otra vez"
pattern = "Hola"
replacement = "Adios"
new_text = re.sub(pattern, replacement, text, count=2, flags=re.IGNORECASE)
print(new_text)


##
# 02 - Metacaracteres
# Los metacaracteres son simbolos especiales con significados específicos en las expresiones regulares

import re
# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva línea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la"

found = re.findall(pattern,text)

if(found):
    print(found)
else:
    print("No se ha encontrado ")

text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"
matches = re.findall(pattern, text)
print(matches)

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la"
found = re.findall(pattern, text)

if(found):
    print(found)
else:
    print("No se ha encontrado el patrón")

# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = " Mi casa es blanca. Y el coche es negro"
pattern = r"\." # anula el significado especial del "."
matches = re.findall(pattern, text)
print(matches)

# \d: coincide con cualquier digito (0-9)

text = "El número  de telefono es 873245687390"
found = re.findall(r'\d{9}', text) #{9} el número de dígitos

print(found)

# Ejercicio detectar si hay un num de España gracias al prefijo +34

text ="mi numero de telefono es +34 934875875 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: 
    print(f"Encontré el numero de telefono {found.group()}")

# \w Coincide con cualquier carácter alfanúmerico (a-z, A-Z, 0-9, _)
text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n ¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern,  text)
print(matches)

# ^:Coincide con el principio de una cadena
username = "423_name%22"
pattern = r"^\w" # Para validar una cadena, obligando que sea un caracter alfanumérico

valid = re.search(pattern, username)

if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

phone = "+43 6989586984"
pattern = r"^\+\d{1,3}"
valid = re.search(pattern, phone)

if valid: print("Es un número de teléfono valido")
else: print("No es un número de teléfono válido")

# $: Coincide con el final de una cadena
text = "Hola mundo."
pattern = r"mundo$"
 
valid = re.search(pattern, text)

if valid: print("La cadena es válida")
else: print("La cadena no es valida")



#EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@gmail.com"
pattern = r"@gmail.com"

valid = re.search(pattern, text)
if valid:("El correo es gmail válido")
else:("No es un correo gmail válido")

#EJERCICIO
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extensión .txt
files = "file1.txt file2.pdf midu-of.wep secret.txt"
pattern = r"\b\w+\.txt\b"

found = re.findall(pattern,files)
print(found)
# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
patter = r"\bc.sa\b"
found = re.findall(patter, text)
print(found)

# |: Coincidir con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7\b}"
found = re.findall(pattern,fruits)
print(found)

##
# Son simbolos especiales con significados específicos en las expresiones regulares

import re
# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva línea

text = "Hola mundo, H0la de nuevo, h$ola otra vez"
pattern = "H.ola"

found = re.findall(pattern,text)
if(found):
    print(found)
else:
    print("No se ha encontrado ")

text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"


# \d: coincide con cualquier digito (0-9)

text = "El número  de telefono es 87324568730"
found = re.findall(r'\d', text)

print(found)

# Ejercicio detectar si hay un num de España
import re
text ="mi numero de telefono es +34 934875875 apuntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: 
    print(f"Encontré el numero de telefono {found.group()}")

#EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@gmail.com"
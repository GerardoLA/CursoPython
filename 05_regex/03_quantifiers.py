###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###
import re
# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern ="a*"
matches = re.findall(pattern,text)
print(matches)

# Ejercicio 1:
# ¿Cuántas palabras tienen de 0 a más "a" y después una b?
text = "aaaba"
pattern =r"a*b"
matches = re.findall(pattern,text)
print(matches)

# +: Una a más veces
text = "dddddd aaa ccc bb"
pattern = "a+"
matches = re.findall(pattern,text)
print(matches)

# ? cero o una vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern,text)
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r"\+?34 \d{9}"
matches = re.findall(pattern, phone)
print(matches)

# {n} Exactamente n veces
text = "aaaaaa     aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)



# {n, m}: de n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern,text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala fantastico casa arbol murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio:
# Encuentras las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)
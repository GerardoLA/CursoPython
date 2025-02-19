



import re
# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern ="a*"
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

# {n, m}: de n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern,text)
print(matches)

words = "ala fantasctico casa arbol murcielago"

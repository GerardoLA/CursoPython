###
# 03 - casting de types
# Transformar un tipo de un valor a otro
###

print("Conversión de tipos:")
print(type(int("100")))

print(2 + int("100"))
print("100" + str(2))

print(float("100.5"))   
print(type(float("100.5")))

print(bool("3"))
print(bool("0"))
print(bool(""))
print(bool(" "))
print(bool("False"))    
print(bool("True"))

# print int("Hola mundo") # ValueError: invalid literal for int() with base 10: 'Hola mundo'
print(round(10.2))


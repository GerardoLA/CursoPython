###
# 0_4 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

# Ejemplo típico de diccionario
persona = {
    "nombre" : "Midudev",
    "edad" : 25,
    "es_estudiante":True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "@midudev",
        "instagram": "@midudev",
        "facebook" : "midudev"
    }
}

# Para acceder a los valores
print(persona["nombre"])
print(persona["edad"])
print(persona["calificaciones"][2])
print(persona["socials"]["instagram"])

# Cambiar valores al acceder
persona["nombre"] = "Tato"
print(persona)

# eliminar completamente una propiedad
del persona["edad"]
print(persona)

es_estudiante = persona.pop("es_estudiante")  # .pop enseña el valor, pero ademas elimina la propiedad del objeto y lo modifica
print(f"es_estudiante:{es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = {"name":"midudev", "age": 25,}
b = {"name": "Leo", "age":36, "es_estudiante": True}

a.update(b)
print(f"El diccionario a, ahora es:{a}")

# comprobar si existe una propiedad
print(("name" in persona)) # False

print(("nombre" in persona)) # True

# obtener todas las claves
print("\nkeys")
print(persona.keys())

# obtener todos los valores
print("\nvalues")
print(persona.values())
# obtener tanto clave como valor
print("\nitems")
print(persona.items())

# pro un lado la llave yt el valor
for key,value in persona.items():
    print(f"{key}:{value}")





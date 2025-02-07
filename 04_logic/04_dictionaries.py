persona = {
    "nombre" : "Midudev",
    "edad" : 25,
    "es_estudiante":True
}

# Para acceder a los valores
print(persona["nombre"])

# Cambiar valores
persona["nombre"] = "Tato"
print(persona)

# eliminar valores
del persona["edad"]
print(persona)


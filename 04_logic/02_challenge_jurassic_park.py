# En Jurassik Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos
# Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosario
# en el parque.

# Importante: Solo se consideran los huevos de dinoasrios carnivoros (T-Rex) aquellos números que son pares.

# Objetivo: 
# Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los que pretencen a los dinosaurios carnivos.
# es decir la sumam de los pares

# Para ver si un número es Par
# siempre usamos el módulo %
# nos da el resto de la división: eggs % 2 == 2

def count_carnivore_dinosar_eggs(egg_list) -> int:
    """ Esta función recibe una lista de números enteros que representan la cantidad de huevos que han puesto diferentes dinosaurios en el parque jurásico y los de número par que son       carnivoros. Devuelve un número con la suma de todos los huevos de carnívoros. """
    
    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs
    return total_carnivore_eggs

# esta forma es más corta:
# total_carnivore_eggs = sum(filter(lambda x: x % 2 == 0, egg_list))

egg_list = [3, 4 , 7, 5, 8]

print(count_carnivore_dinosar_eggs(egg_list))


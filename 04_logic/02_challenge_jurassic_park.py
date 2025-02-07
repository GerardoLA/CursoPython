# En Jurassik Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos
# Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevospuestos por un dinosario
# en el parque.

# Importante: Solo se consideran los huevos de dinoasrios carnivoros (T-Rex) aquellos números que son pares.

# Objetivo: 
# Escribe una función en Python qeu reciba una lista de números enteros y devuelva la suma total de los que pretencen a los dinosaurios carnivos.
# es decir la sumam de los pares

def count_carnivore_dinosar_eggs(egg_list) -> int:
    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs
    return total_carnivore_eggs

egg_list = [3, 4 , 7, 5, 8]

print(count_carnivore_dinosar_eggs(egg_list))
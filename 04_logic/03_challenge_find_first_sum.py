"""
Dado un array de numeros y un numero goal, encuentra los dos primeros nombres del array que sumen el número goal y devuelve sus índices
Si no exite tal combinacion, devuelve None
nums =  [4, 5, 6, 2]
goal =  8

find_first_sum(nums,goal)

"""
# def find_first_sum(nums, goal):
#     if len(nums) == 0:return None
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#           if nums[i] + nums[j] == goal:
#              return[i, j] 
#     return None  # no se encontró ninguna combinación

# Se puede hacer mejor con un diccionario:

def find_first_sum(nums, goal):
    seen = {} # diccionario para guardar el número y su índice

    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return [seen[missing], index]
        seen[value] = index # guardar el número actual a los vistos, porque no hemos encontrado la combinación
    
    return None

        

nums =  [4, 5, 6, 2]
goal = 8
    
result = find_first_sum(nums, goal)
print(result)

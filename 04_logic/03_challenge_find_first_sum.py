"""
Dado unarray de numeros y un numero goal, encuentttra los dos primeros nombres del array que sumen el numerpo goal y devuelve sus indices
Si no exite tal combinacion, devuelve
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
#     return None  

def find_first_sum(nums, goal):
    seen = {} # diccionario para guardar el número y su índice

    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return seen

        print(f"index:{index} value: {value}")

nums =  [4, 5, 6, 2]
goal = 8
    
result = find_first_sum(nums, goal)
print(result)

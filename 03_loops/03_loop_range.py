###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print("\nrange(): ")

nums = range(10)
for num in nums:
    print(num)

# range(inicio,fin)
for num in range(5, 10):
    print(num)

# range(inicio, fin, paso)
for num in range(0, 10, 2):
    print(num)

for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

#para hacer lista
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# para hacerlo cinco veces
for _ in range(5):
    print("Hacer cinco veces algo")
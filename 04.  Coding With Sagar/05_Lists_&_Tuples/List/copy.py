print()
list_1 = [1,2,3]
list_2 = list_1.copy()
list_2[0] = 100

print(list_1) # [1, 2, 3]
print(list_2) # [100, 2, 3]

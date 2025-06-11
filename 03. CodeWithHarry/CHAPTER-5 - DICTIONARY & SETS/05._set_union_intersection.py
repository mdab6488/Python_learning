s1 = {1, 45, 6, 2}
s2 = {7, 8, 1, 78, 2}

print()
print(f"S1: {s1} Lenght: {len(s1)}")
print(f"S2: {s2} Lenght: {len(s2)}")
print()
union_value = s1.union(s2)
print(f"Union: {union_value}\nLenght: {len(union_value)}")
print()
intersection_value = s1.intersection(s2)
print(f"Intersection: {intersection_value}\nLenght: {len(intersection_value)}")
print(f"\n{"*" * 30}\n")
print(s1 - s2)
print(s2 - s1)

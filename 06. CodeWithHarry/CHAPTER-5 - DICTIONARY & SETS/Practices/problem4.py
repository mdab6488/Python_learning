s = set()
s.add(20)
s.add(20.0)
s.add("20")

print()
print(s) # {20, '20'}
print(f"Length: {len(s)}") # 2
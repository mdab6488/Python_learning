a: int = 89 # Global a
def fun():
    a: int = 3 # Local a
    print(a)

print()
# a = 89 # Global a
print(a) # 89
fun()
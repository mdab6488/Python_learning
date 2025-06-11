# 5! = 1 X 2 X 3 X 4 X 5

print()
n = int(input("Enter the number: "))

product = 1
for i in range(1, n+1):
    prev_product = product
    product *= i
    print(f"-> {prev_product} * {i} = {product}")


print(f"The factorial if {n} is {product}")
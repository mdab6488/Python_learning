# Using walrus operator
if n := len([1,2,3,4,5]) > 3:
    print(f"List is too ling ({n} elements, expected <= 3)")

#Outpurt: List is too long (5 elements, expected <= 3)
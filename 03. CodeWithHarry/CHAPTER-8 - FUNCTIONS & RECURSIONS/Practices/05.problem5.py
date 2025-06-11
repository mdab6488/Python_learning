print()

def pattern_fun(num):
    if num==0:
        return
    print("*" * num)
    pattern_fun(num-1)

n = int(input("Enter the number: "))

pattern_fun(n)
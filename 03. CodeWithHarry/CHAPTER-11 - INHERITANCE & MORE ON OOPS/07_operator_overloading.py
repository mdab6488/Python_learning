class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, num):
        return self.number + num.number

n = Number(1)
m = Number(2)

print()
print(n + m)
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in
from math import e

print(f"{"*" * 24}")
print(f"{" " * 8} local {" " * 8}")
print(f"{"*" * 24}")
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

def happy_birthday(name, age):
    print(f"Happy birthday dear {name}")
    print(f"Your age {age} years old")

def main():
    name = "Riyan"
    age = 23
    happy_birthday(name, age)

main()

print(f"{"*" * 24}")
print(f"{" " * 7} Enclosed {" " * 7}")
print(f"{"*" * 24}")
def func3():
    x = 1

    def func4():
        x = 2
        print(x)
    func4()

func3()

print(f"{"*" * 24}")
print(f"{" " * 8} Global {" " * 8}")
print(f"{"*" * 24}")
def func5():
    print(x)

def func6():
    print(x)

x = 3
func5()
func6()

print(f"{"*" * 24}")
print(f"{" " * 8} Built-in {" " * 8}")
print(f"{"*" * 24}")
# print(e)

def func7():
    print(e)

e = 3

func7()
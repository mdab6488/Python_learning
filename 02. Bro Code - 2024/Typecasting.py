# Typecasting = the process of converting a variable from one data type to another
#             = str(), int(), float(), bool()

name = "MD ABDUR RAHMAN"
age = 27
gpa = 3.12
is_student = False

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

print("*" * 30)
print("Concert The variables")
print("*" * 30)

gpa = int(gpa)
print(type(gpa))
print(gpa)

age = float(age)
print(type(age))
print(age)

age = 27

age = str(age)
# age += 1 # TypeError: can only concatenate str (not "int") to str
age += "1"
print(type(age))
print(age)

name = ""

name = bool(name)
print(type(name))
print(name)

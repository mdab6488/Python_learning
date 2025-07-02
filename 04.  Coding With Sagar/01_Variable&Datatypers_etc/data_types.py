print()
"""
Numeric Type
int - whole numbers 100 200 -100
float - decimal numbers 1.145 -10.55
complex - real & imaginary part
a+bj
3+4j
"""
a = 10
b = 10.40
c = 3+4j

print(f"Numeric Type: {a}, {b}, {c}")
# print(type(a)) # <class 'int'>
# print(type(b)) # <class 'float'>
# print(type(c)) # <class 'complex'>

"""
Boolean Type
True/False - logical operations
"""
print()
is_raining = True
is_sunny = False
print(f"Boolean Types: {is_raining}, {is_sunny}")
# print(type(is_raining)) # <class 'bool'>
# print(type(is_sunny)) # <class 'bool'>

"""
None Type
"""
print()
result = None
print(f"None Types: {result}")

"""
Sequences Data Type
1. string - "data" 'data'
2. list - []
3. tuple - () Can not modified
"""
print()
text = "MD ABDUR RAHMAN"
print(f"String Type: {text}")
# print(type(text)) # <class 'str'>

print()
names = ["Riyan", "MD AB", "Alamin", "MD ABDUR RAHMAN"]
print(f"list Type: {names}")
# print(type(names)) # <class 'list'>

print()
locations = ("Uttara", "ECB", "Matikata", "Vashantak", "ECB") # ('Uttara', 'ECB', 'Matikata', 'Vashantak', 'ECB')
print(f"tuple Type: {locations}")
# print(type(locations)) # <class 'tuple'>


"""
Set Data Type
1. set(mutable) {}
2. frozenset(immutable)
"""
print()
unique_number = {1, 2, 3, 4, 5, 6, 1, 2, 5, 3, 5, 3, 4, 2}
print(f"set() for Unique Numbers: {unique_number}")
# set() for Unique Numbers: {1, 2, 3, 4, 5, 6}
print(type(unique_number)) # <class 'set'>

print()
immutable_set = frozenset([1, 2, 3, 4, 5, 4,5, 4,2, 2])
print(f"frozenset() for Immutable Set: {immutable_set}")
# frozenset() for Immutable Set: frozenset({1, 2, 3, 4, 5})
# print(type(immutable_set)) # <class 'frozenset'>

"""
Mapping Data Type
pair
key:value, key:values
1. dictionary/dict - {}
"""
print()
person = {
    "name": "Alamin",
    "age": 10000000000000000000000000000,
    "number": "01974127728", 100:100.100
}
print(f"Dictionary Type: {person}")
print(type(person))
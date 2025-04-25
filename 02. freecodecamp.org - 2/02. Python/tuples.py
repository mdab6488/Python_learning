# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are similar to lists, but they cannot be changed after creation. They are defined by enclosing the elements in parentheses `()`.
# Tuples can contain any type of data, including other tuples, lists, and dictionaries.
# Tuples are often used to group related data together, such as coordinates (x, y) or RGB color values (r, g, b).
# Tuples can also be used as keys in dictionaries, while lists cannot.
# Tuples are faster than lists for certain operations, such as iteration and membership testing.
# Tuples are defined using parentheses `()` and can contain any number of elements, including zero.
# Tuples can be nested, meaning that a tuple can contain other tuples as elements.

from pprint import pprint

names = ("Riyan", "Alamin")

names[0]
names.index("Alamin")

pprint(len(names))

pprint("Alamin" in names)

pprint(sorted(names))

newTuple = names + ("Name1", "Name2")

pprint(newTuple)

# keyword arguments = an argument preceded by an identifier
#                     help with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4, arbitary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", first="Riyan", last="Kabir", title="Mr.")

for x in range(1, 11):
    print(x, end=" ")

print()

print("1", "2", "3", "4", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country=1, area=123, first=456, last=7890)
print(phone_number)
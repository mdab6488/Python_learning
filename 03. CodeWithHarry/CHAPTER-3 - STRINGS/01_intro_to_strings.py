a ='Riyan Kabir' # Single quoted string
b = "MD ABDUR RAHMAN" # Double-quoted string
c = '''Alamin''' # Triple quoted string

len_1 = len(a)
len_2 = len(b)
len_3 = len(c)

print(f"A = {len_1}, B = {len_2}, C = {len_3}")

# firstName = a[ind_start:ind_end]
firstName = a[:5]
lastName = a[-5:-1]
lastName2 = a[-5:]
print(firstName)
print(lastName)
print(lastName2)

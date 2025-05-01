# format specifiers = {value:flags} format a value based-on-what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate are zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space befor positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

price4 = 3000.14159
price5 = -9870.65
price6 = 1200.34

# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 1 is ${price2:.3f}")
# print(f"Price 1 is ${price3:.4f}")

# print(f"Price 1 is ${price1:10}") # add 10 spaces
# print(f"Price 1 is ${price2:010}") # Price 1 is $-000987.65
# print(f"Price 1 is ${price3:<10}") # Left justified then add 10 spaces

# print(f"Price 1 is ${price1:>10}") # Right justified then add 10 spaces
# print(f"Price 1 is ${price2:>10}") # Right justified then add 10 spaces
# print(f"Price 1 is ${price3:>10}") # Right justified then add 10 spaces
#
# print(f"Price 1 is ${price1:^10}") # For Center
# print(f"Price 1 is ${price2:^10}") # For Center
# print(f"Price 1 is ${price3:^10}") # For Center

# print(f"Price 1 is ${price1:+}") # Price 1 is $+3.14159
# print(f"Price 1 is ${price2:+}") # Price 1 is $-987.65
# print(f"Price 1 is ${price3:+}") # Price 1 is $+12.34

# print(f"Price 1 is ${price1: }") # Price 1 is $ 3.14159
# print(f"Price 1 is ${price2: }") # Price 1 is $-987.65
# print(f"Price 1 is ${price3: }") # Price 1 is $ 12.34

# print(f"Price 1 is ${price4:,}") # Price 1 is $3,000.14159
# print(f"Price 1 is ${price5:,}") # Price 1 is $-9,870.65
# print(f"Price 1 is ${price6:,}") # Price 1 is $1,200.34

# print(f"Price 1 is ${price4:,.2f}") # Price 1 is $3,000.14
# print(f"Price 1 is ${price5:,.2f}") # Price 1 is $-9,870.65
# print(f"Price 1 is ${price6:,.2f}") # Price 1 is $1,200.34

print(f"Price 1 is ${price4:+,.2f}") # Price 1 is $+3,000.14
print(f"Price 1 is ${price5:+,.2f}") # Price 1 is $-9,870.65
print(f"Price 1 is ${price6:+,.2f}") # Price 1 is $+1,200.34
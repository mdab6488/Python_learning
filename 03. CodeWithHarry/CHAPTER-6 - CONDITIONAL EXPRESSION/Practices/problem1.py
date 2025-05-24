print()
numbers = []

for i in range(4):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

number1 = numbers[0]
number2 = numbers[1]
number3 = numbers[2]
number4 = numbers[3]

if number1>number2 and number1>number3 and number1>number4:
    print("#1️⃣st is the Greatest number: ", number1)

elif number2>number1 and number2>number3 and number2>number4:
    print("#2️⃣nd is the Greatest number: ", number2)

elif number3>number1 and number3>number2 and number3>number4:
    print("#3️⃣rd is the Greatest number: ", number3)

elif number4>number1 and number4>number2 and number4>number3:
    print("#4️⃣th is the Greatest number: ", number4)
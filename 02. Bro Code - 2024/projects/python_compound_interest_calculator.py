principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle ammount: "))
#     if principle <= 0:
#         print("Principle can't be less then or equal to zeor")
#
# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interset rate can't be less then or equal to zeor")
#
# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less then or equal to zeor")

while True:
    principle = float(input("Enter the principle ammount: "))
    if principle < 0:
        print("Principle can't be less then zeor")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interset rate can't be less then zeor")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less then zeor")
    else:
        break

# print(principle)
# print(rate)
# print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
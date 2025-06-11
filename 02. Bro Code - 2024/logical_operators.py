 # logical operators = evaluate multiple conditions (or, and, not)
 #                     or = at least one condition must be True
 #                     and = both conditions must be True
 #                     not = inverts the condition (not False, not True)

print("*" * 30)
print(f"{' ' * 13} OR {' ' * 13}")
print("*" * 30)

temp = 20
is_raning = False

if temp > 35 or temp < 0 or is_raning:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

print("*" * 30)
print(f"{' ' * 13} AND {' ' * 13}")
print("*" * 30)

temp2 = 18
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif temp2 <= 0 and is_sunny:
    print("It is COLD OUTSIDE 🥶")
    print("It is SUNNY ☀️")
# elif temp2 < 28 and temp > 0 and is_sunny:
elif 28 > temp2 > 0 and is_sunny:
    print("It is WARM OUTSIDE 🪖")
    print("It is SUNNY ☀️")


print("*" * 30)
print(f"{' ' * 13} NOT {' ' * 13}")
print("*" * 30)

temp3 = 20
is_sunny = False

if temp3 >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY 🌧️")
elif temp3 <= 0 and not is_sunny:
    print("It is COLD OUTSIDE 🥶")
    print("It is CLOUDY 🌧️")
# elif temp3 < 28 and temp > 0 and is_sunny:
elif 28 > temp3 > 0 and not is_sunny:
    print("It is WARM OUTSIDE 🪖")
    print("It is CLOUDY 🌧️")


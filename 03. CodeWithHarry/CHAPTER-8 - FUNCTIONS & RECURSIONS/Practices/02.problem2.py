print()

def f_to_c(temp):
   return 5 * (temp - 32) / 9

f = int(input("Enter temprature in F: "))
c = f_to_c(f)
print(f"{c:.2f}°C")
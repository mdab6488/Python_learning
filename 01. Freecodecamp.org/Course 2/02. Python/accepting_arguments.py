# import sys

# print("hello world")

# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py
# hello world

# print(sys.argv)
# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py alamin 27
# ['accepting_arguments.py', 'alamin', '27']

# name = sys.argv[1]
# print(f"Hello {name}")
# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py alamin
# Hello alamin

import argparse

parser = argparse.ArgumentParser(description="This program prints the name of my dogs")

parser.add_argument(
    "-c",
    "--color",
    metavar="color",
    required=True,
    choices={"red", "blue"},
    help="the color to search for",
)

args = parser.parse_args()

print(args.color)
# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py -c Red
# Red

# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py
# usage: accepting_arguments.py [-h] -c color
# accepting_arguments.py: error: the following arguments are required: -c/--color

# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py -c Blue
# usage: accepting_arguments.py [-h] -c color
# accepting_arguments.py: error: argument -c/--color: invalid choice: 'Blue' (choose from red, blue)
# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py -c blue
# blue
# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py -c red
# red
# C:\00_MDAB\Learning\Python_learning\02. freecodecamp.org - 2\02. Python> py accepting_arguments.py -c orange
# usage: accepting_arguments.py [-h] -c color
# accepting_arguments.py: error: argument -c/--color: invalid choice: 'orange' (choose from blue, red)

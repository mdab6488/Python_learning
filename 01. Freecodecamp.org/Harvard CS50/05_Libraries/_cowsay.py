# pip install cowsay

from sys import argv
from cowsay import cow, trex

if len(argv) == 2:
    cow("Hello, " + argv[1])
    trex("Hello, " + argv[1])
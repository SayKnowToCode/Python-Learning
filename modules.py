from math import pi
import sys
import random as rdm
import kansas
import cli

print(pi)

for item in dir(rdm):
    print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

cli.hello("Dave", "Spanish")
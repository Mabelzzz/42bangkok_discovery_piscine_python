#!/usr/bin/env python3
import math
try:
    number = float(input("Give me a number: "))
    print(math.ceil(number))
except:
    print("Error: Invalid input cuz' it's not a number")

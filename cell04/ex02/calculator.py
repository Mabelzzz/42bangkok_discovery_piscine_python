#!/usr/bin/env python3
try:
	first = int(input("Give me a first number: "))
	second = int(input("Give me a second: "))
	print("Thank you!")
	print(f"{first} + {second} = {first + second}")
	print(f"{first} - {second} = {first - second}")
	print(f"{first} / {second} = {first / second}")
	print(f"{first} * {second} = {first * second}")
except:
    print("Error: Invalid input cuz' it's not an integer")



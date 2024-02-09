#!/usr/bin/env python3
try:
	number = float(input("Give me a number: "))
	if number % 1 == 0:
		print("This number is an integer.")
	else:
		print("This number is an decimal.")
except:
    print("Error: Invalid input cuz' it's not a number")

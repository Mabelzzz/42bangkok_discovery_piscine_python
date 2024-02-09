#!/usr/bin/env python3
try:
	firstNbr = int(input("Enter the first number:\n"))
	secondNbr = int(input("Enter the second number:\n"))
	ans = firstNbr * secondNbr
	print(f"{firstNbr} x {secondNbr} = {ans}")
	if ans == 0:
		print("The result is positive and negative.")
	elif ans < 0:
		print("The result is negative.")
	else:
		print("The result is positive.")
except ValueError:
	print("Error: Invalid input cuz' it's not an integer")

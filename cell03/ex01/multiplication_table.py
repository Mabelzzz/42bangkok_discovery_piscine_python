#!/usr/bin/env python3
try:
	number = int(input("Enter a number\n"))
	for i in range(0, 10):
		print(f"{i} x {number} = {i * number}")
except:
	print("Error: Invalid input cuz' it's not an integer")


#!/usr/bin/env python3
try:
	number = int(input("Enter a number less than 25\n"))
	if number > 25:
		print("Error")
	else:
		for number in range(number, 26):
			print(f"Inside the loop, my variable is {number}")
except:
	print("Error: Invalid input cuz' it's not an integer")

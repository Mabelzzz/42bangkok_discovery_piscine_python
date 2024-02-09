#!/usr/bin/env python3
try:
	number = float(input())
	if number == 0:
		print("This number is equal to zero.")
	else:
		print("This number is different from zero.")
except ValueError:
	print("Not a number")


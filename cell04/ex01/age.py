#!/usr/bin/env python3
try:
	age = int(input("Please tell me your age: "))
	print(f"You are currently {age} years old.")
	for i in range (10, 31, 10):
		print(f"In {i} years, you'll be {age + i} years old.")
except:
	print("Error: Invalid input cuz' it's not an integer")

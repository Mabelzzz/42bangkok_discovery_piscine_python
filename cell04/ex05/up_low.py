#!/usr/bin/env python3
try:
	string = input()
	for ch in string:
		if ch.islower() == True:
			print(ch.upper(), end="")
		elif ch.isupper() == True:
			print(ch.lower(), end="")
		else:
			print(ch, end="")
	print("")
except:
    print("\nError")

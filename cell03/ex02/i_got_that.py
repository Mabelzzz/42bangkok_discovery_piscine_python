#!/usr/bin/env python3
try:
	response = input("What you gotta say? : ")
	while response != "STOP":
		response = input("I got that! Anything else? : ")
except:
    print("\nEXIT")


#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
	str = input("What was the parameter? ")
	if str == sys.argv[1]:
		print("Good Job!")
	else:
		print("Nope, sorry...")
else:
    print("none")

#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
	for i in range (0, 11):
		print(f"Table de {i}:", end=" ")
		for j in range(0, 11):
			if j == 10:
				print(i * j)
			else:
				print(i * j, end=" ")
else:
	print("none")

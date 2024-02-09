#!/usr/bin/env python3
import sys

def main():
	if len(sys.argv) != 3:
		print('none')
	else:
		try:
			start = int(sys.argv[1])
			end = int(sys.argv[2])

			if start <= end:
				print(list(range(start, end + 1)))
			else:
				print(list(range(end, start + 1)))

		except:
			print("\nEXIT ERROR")

if __name__ == "__main__":
	main()

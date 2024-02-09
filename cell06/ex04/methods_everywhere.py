#!/usr/bin/env python3
import sys

try:
	class StringModifier:
		def shrink(self, s):
			print(s[:8])

		def enlarge(self, s):
			print(s + 'Z' * (8 - len(s)))

	def main():
		modifier = StringModifier()
		if len(sys.argv) <= 1:
			print('none')
		else:
			for i in sys.argv[1:]:
				if len(i) > 8:
					modifier.shrink(i)
				elif len(i) < 8:
					modifier.enlarge(i)
				else:
					print(i)

	if __name__ == "__main__":
		main()
except:
    print("\nEXIT ERROR")

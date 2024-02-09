#!/usr/bin/env python3

try:
	class AddAge:
		def add_one(n):
			n += 1
			return n

	def main():
		my_variable = 67
		print("Before calling add_one:", my_variable)
		my_variable = AddAge.add_one(my_variable)
		print("After calling add_one:", my_variable)

	if __name__ == "__main__":
		main()
except:
    print("\nEXIT ERROR")

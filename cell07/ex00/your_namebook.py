#!/usr/bin/env python3

try:
	class NameBook:
		def array_of_names(person_dict):
			full_names = []
			for first_name, last_name in person_dict.items():
				full_name = first_name.capitalize() + ' ' + last_name.capitalize()
				full_names.append(full_name)
			return full_names

	persons = {
		"jean": "valjean",
		"grace": "hopper",
		"xavier": "niel",
		"fifi": "brindacier"
	}
	print(NameBook.array_of_names(persons))

except:
	print("\nEXIT ERROR")

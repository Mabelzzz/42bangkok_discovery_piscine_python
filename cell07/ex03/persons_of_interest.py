#!/usr/bin/env python3

try:
	class HistoricalFigures:
		def sort_by_birthdate(person):
			return person['date_of_birth']

		def famous_births(people_dict):
			people_list = list(people_dict.values())
			sorted_people = sorted(people_list, key=HistoricalFigures.sort_by_birthdate)
			for person in sorted_people:
				print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

	women_scientists = {
		"ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
		"cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
		"lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
		"grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
	}

	HistoricalFigures.famous_births(women_scientists)

except:
	print("\nEXIT ERROR")

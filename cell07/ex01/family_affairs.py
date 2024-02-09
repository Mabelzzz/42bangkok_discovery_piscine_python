#!/usr/bin/env python3

try:
	class FamilyAffairs:
		def find_the_redheads(family_dict):
			redheads = []
			for name in family_dict.keys():
				if family_dict[name] == 'red':
					redheads.append(name)
			return redheads

	dupont_family = {
		"florian": "red",
		"marie": "blond",
		"virginie": "brunette",
		"david": "red",
		"franck": "red"
	}
	print(FamilyAffairs.find_the_redheads(dupont_family))

except:
	print("\nEXIT ERROR")

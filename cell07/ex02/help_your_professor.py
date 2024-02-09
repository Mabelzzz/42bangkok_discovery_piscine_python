#!/usr/bin/env python3

try:
	class ScoreCalculator:
		def average(scores_dict):
			total_score = sum(scores_dict.values())
			num_students = len(scores_dict)

			if num_students == 0:
				return 0
			else:
				return total_score / num_students

	class_3B = {
		"marine": 18,
		"jean": 15,
		"coline": 8,
		"luc": 9
	}

	class_3C = {
		"quentin": 17,
		"julie": 15,
		"marc": 8,
		"stephanie": 13
	}
	print(f"Average for class 3B: {ScoreCalculator.average(class_3B)}.")
	print(f"Average for class 3C: {ScoreCalculator.average(class_3C)}.")

except:
	print("\nEXIT ERROR")

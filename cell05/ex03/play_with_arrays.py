#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {original_array}")

new_set = {num + 2 for num in original_array if num > 5}
print(f"New set: {new_set}")

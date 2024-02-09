#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3:
	found = re.findall(sys.argv[1], sys.argv[2])
	if len(found) > 0:
		print(len(found)); sys.exit(0)
print("none")

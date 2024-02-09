#!/usr/bin/env python3
import sys

len = len(sys.argv)
if len <= 2:
	print("none")
else:
    for i in range(len - 1, 0, -1):
        print(sys.argv[i])


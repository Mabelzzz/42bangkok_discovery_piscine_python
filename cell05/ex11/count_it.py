#!/usr/bin/env python3
import sys

if len(sys.argv) <= 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for i, j in enumerate(sys.argv):
        if i > 0:
        	print(f"{j}: {len(j)}")

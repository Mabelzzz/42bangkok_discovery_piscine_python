#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    if sys.argv[1].find("z") == -1:
        print("none")
    else:
        for i in sys.argv[1]:
            if i == 'z':
                print(i, end="")
else:
    print("none")



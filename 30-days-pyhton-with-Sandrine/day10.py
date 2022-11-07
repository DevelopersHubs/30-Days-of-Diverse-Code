#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
DATA = bin(n)

maximum = 0
first = 0

for num in DATA:
    if num == '1':
        first = first + 1
    else:
        maximum = max(maximum, first)
        first = 0

print(max(maximum, first))
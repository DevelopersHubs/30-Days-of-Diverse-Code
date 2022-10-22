#!/bin/python3

import math
import os
import random
import re
import sys
#define a function named mul. and perform 
# the multiplication table of any particular number
def mul(n):
    for i in range(1,11):
        result = n*i
        print(n,'x',i,'=', result)

if __name__ == '__main__':
    n = int(input().strip())
    mul(n)
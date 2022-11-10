#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
# Write Your Code Here
swap = 0
swap_first = True

while swap_first:
    swap_first = False
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            swap+= 1
            swap_first = True

print('Array is sorted in {} swaps.'.format(swap))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))
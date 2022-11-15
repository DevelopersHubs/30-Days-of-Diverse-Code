#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    LIST = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if emailID.endswith("@gmail.com"):
            LIST.append(firstName)

    LIST.sort()
    for val in LIST:
        print(val)
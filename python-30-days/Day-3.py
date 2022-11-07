#!/bin/python3

import math
import os
import random
import re
import sys
def mat(N):
    
    if(N%2 != 0):
        print("Weird")
    elif(N%2 == 0 & 2<=N<=5):
        print("Not Weird")
    elif(N%2 == 0 & 6<=N<=20):
        print("Weird")
    elif(N%2 == 0 & N>20):
        print("Not Weird")
    else:
        print('Not Weird')
  
if __name__ == '__main__':
    N = int(input().strip())
    mat(N)

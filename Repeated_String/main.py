#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    index = []; total_str = int(n/len(s)); rest = n%len(s)
    num = s.count('a')
    total = int(num*total_str)
    for i in range(0, len(s)):
        if s[i] == 'a':
            index.append(i+1)
    indx = list(index)
    for j in range (0,len(indx)):
        if int(indx[j]) <= rest:
            total+=1
        else:
            break
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

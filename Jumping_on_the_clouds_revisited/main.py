#!/bin/python3
import os

def jumpingOnClouds(c, k):
    e=100; i = 0; b = False
    while i!=0 or b == False:
        b = True
        if c[i] == 1:
            e-=2
        e-=1
        i+=k
        i = i%len(c)
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the triplets function below.

    
 
def triplets(a, b, c):
    a, b, c = list(sorted(set(a))), list(sorted(set(b))), list(sorted(set(c)))
    res = 0
    for i in b:
        a_i = bisect.bisect_right(a, i)
        c_i = bisect.bisect_right(c, i)
        res += (a_i*c_i)
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

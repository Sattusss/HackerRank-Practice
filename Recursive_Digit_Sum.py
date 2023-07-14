import math
import os
import random
import re
import sys

def superDigit(n, k):
    if len(n) == 1:
        return int(n)
    else:
        return superDigit(str(sum([int(i) for i in n]) * k), 1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
    
import math
import os
import random
import re
import sys

def pairs(k, arr):
    arr.sort()
    count = 0
    i = 0
    j = 1
    while j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k:
            count += 1
            j += 1
        elif diff > k:
            i += 1
        else:
            j += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()

    
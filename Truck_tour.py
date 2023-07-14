import math
import os
import random
import re
import sys

def truckTour(petrolpumps):
    start = 0
    petrol = 0
    for i in range(len(petrolpumps)):
        petrol += petrolpumps[i][0] - petrolpumps[i][1]
        if petrol < 0:
            start = i + 1
            petrol = 0
    return start

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    result = truckTour(petrolpumps)
    fptr.write(str(result) + '\n')
    fptr.close()
    
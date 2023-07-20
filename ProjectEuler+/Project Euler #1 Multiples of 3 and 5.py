import math
import os
import random
import re
import sys

def sumOfMultiples(n, k):
    p = (n-1)//k
    return k*(p*(p+1))//2

def sumOfMultiplesOf3And5(n):
    return sumOfMultiples(n, 3) + sumOfMultiples(n, 5) - sumOfMultiples(n, 15)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print(sumOfMultiplesOf3And5(n))

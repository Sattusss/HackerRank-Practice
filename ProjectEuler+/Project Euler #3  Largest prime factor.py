import math
import os
import random
import re
import sys

def largestPrimeFactor(n):
    p = 2
    while p*p <= n:
        while n % p == 0:
            n //= p
        p += 1
    return n

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print(largestPrimeFactor(n))
        
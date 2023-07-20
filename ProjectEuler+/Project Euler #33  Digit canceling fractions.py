import math 
import os
import random
import re
import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def digitCancellingFractions(n):
    num = 1
    den = 1
    for a in range(1, 10):
        for b in range(1, a):
            for c in range(1, 10):
                if (10*b+a)*c == (10*a+c)*b:
                    num *= b
                    den *= c
    return den//gcd(num, den)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print(digitCancellingFractions(n))
        
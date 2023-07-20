#!/bin/python3

import math
import os
import random
import re
import sys

def sumOfEvenFibonacciNumbers(n):
    a = 1
    b = 2
    s = 0
    while b <= n:
        if b % 2 == 0:
            s += b
        a, b = b, a+b
    return s

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print(sumOfEvenFibonacciNumbers(n))
        



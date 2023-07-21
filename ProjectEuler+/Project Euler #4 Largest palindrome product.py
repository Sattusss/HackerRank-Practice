import math
import os
import random   
import re
import sys

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def Palindrome_Prod(N):
    for num in range(N - 1, 100000, -1):
        if is_palindrome(num):
            for i in range(999, 99, -1):
                if num % i == 0 and num // i < 1000:
                    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = Palindrome_Prod(n)
        fptr.write(str(result) + '\n')
    fptr.close()

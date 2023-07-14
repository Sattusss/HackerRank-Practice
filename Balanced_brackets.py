import math
import os
import random
import re
import sys

def isBalanced(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 'NO'
            if c == ')' and stack[-1] != '(':
                return 'NO'
            if c == ']' and stack[-1] != '[':
                return 'NO'
            if c == '}' and stack[-1] != '{':
                return 'NO'
            stack.pop()
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
    

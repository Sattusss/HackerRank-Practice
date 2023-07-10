import math
import os
import random
import re
import sys

def flippingMatrix(matrix):
    n = len(matrix)
    result = 0
    for i in range(n//2):
        for j in range(n//2):
            result += max(matrix[i][j], matrix[i][n-1-j], matrix[n-1-i][j], matrix[n-1-i][n-1-j])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        matrix = []
        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))
        result = flippingMatrix(matrix)
        fptr.write(str(result) + '\n')
    fptr.close()
    
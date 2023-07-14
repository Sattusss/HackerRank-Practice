import math
import os
import random
import re
import sys

def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                count += 1
    print(count)
    return

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
        
import math
import os
import random
import re
import sys

def simpleTextEditor(queries):
    s = ''
    stack = []
    for i in range(len(queries)):
        query = queries[i].split()
        if query[0] == '1':
            stack.append(s)
            s += query[1]
        elif query[0] == '2':
            stack.append(s)
            s = s[:-int(query[1])]
        elif query[0] == '3':
            print(s[int(query[1]) - 1])
        else:
            s = stack.pop()

if __name__ == '__main__':
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(input())
    simpleTextEditor(queries)

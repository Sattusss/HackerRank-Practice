import math
import os
import random
import re
import sys
from collections import defaultdict, deque


def bfs(n, m, edges, s):
    graph = defaultdict(list)
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    dists = defaultdict(lambda: -1)
    dists[s] = 0
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if dists[neighbor] < 0:
                queue.append(neighbor)
                dists[neighbor] = dists[v] + 6
    return [dists[i] for i in range(1, n+1) if i != s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))
        s = int(input())
        result = bfs(n, m, edges, s)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

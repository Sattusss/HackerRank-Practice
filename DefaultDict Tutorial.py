import collections

n, m = map(int, input().split())
d = collections.defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    print(*d[input()] or [-1])

    
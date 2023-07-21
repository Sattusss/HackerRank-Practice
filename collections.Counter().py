import collections

numshoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numcust = int(input())

income = 0

for i in range(numcust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)

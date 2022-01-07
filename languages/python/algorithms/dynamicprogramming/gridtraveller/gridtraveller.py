#!/usr/bin/env python3


def gridtraveller(m, n):
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        return gridtraveller(m-1, n) + gridtraveller(m, n-1)


print(gridtraveller(1, 1))
print(gridtraveller(2, 3))
print(gridtraveller(3, 2))
print(gridtraveller(3, 3))
# print(gridtraveller(18, 18)) # This takes too much time. Should use memoization


def gridtravellerMemoize(m, n, mem={}):
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    elif (m, n) in mem:
        return mem[(m, n)]
    elif (n, m) in mem:
        return mem[(n, m)]        
    else:
        result = gridtravellerMemoize(m-1, n, mem) + gridtravellerMemoize(m, n-1, mem)
        mem[(m,n)] = result
        return result


print(gridtravellerMemoize(1, 1))
print(gridtravellerMemoize(2, 3))
print(gridtravellerMemoize(3, 2))
print(gridtravellerMemoize(3, 3))
print(gridtravellerMemoize(18, 18))

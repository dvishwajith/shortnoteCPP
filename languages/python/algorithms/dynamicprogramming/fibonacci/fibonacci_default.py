#!/usr/bin/env python3

def fib(n):
    if n <= 2:
        return 1

    else:
        return fib(n-1) + fib(n-2)


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(6))
print(fib(8))

#print(fib(50))  This is Quadtrallions . need 2^50 steps

###################using Memoisation##########################


def fib_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        memo[n] = 1
        return 1
    else:
        val = fib_memoized(n-1, memo) + fib_memoized(n-2, memo)
        memo[n] = val
        return val


print('\fib_memoized')
print(fib_memoized(1))
print(fib_memoized(2))
print(fib_memoized(3))
print(fib_memoized(6))
print(fib_memoized(8))

print(fib_memoized(50)) 


#finonacci tabulation



def fib_tabulation(n):
    dp = [0 for i in range(n+2)]
    dp[0] = 0
    dp[1] = 1

    for i in range(n):
        dp[i+1] = dp[i+1] + dp[i]
        dp[i+2] = dp[i+2] + dp[i]

    return dp[n]

print('\nfib_tabulation')
print(fib_tabulation(1))
print(fib_tabulation(2))
print(fib_tabulation(3))
print(fib_tabulation(6))
print(fib_tabulation(8))

print(fib_tabulation(50)) 

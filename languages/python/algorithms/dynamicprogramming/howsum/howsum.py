#!/usr/bin/env python3


def howsum(sum, values=[]):
    how_list = []
    for val in values:
        if sum - val == 0:
            how_list.append(val)
            return how_list
        elif sum - val > 0:
            partial_sum_list = howsum(sum - val, values)
            if len(partial_sum_list) > 0:
                partial_sum_list.append(val)
                return partial_sum_list
    return how_list

print("howsume method 1")
print(howsum(7, [5,3,4,7]))
print(howsum(7, [2,4]))
print(howsum(7, [2,4,1]))
print(howsum(8, [2,3,5]))

def howsummethod2(sum, values=[]):
    if sum is 0:
        return []
    elif sum < 0:
        return None
    else:
        howlist = None
        for val in values:
            howlist = howsummethod2(sum - val, values)
            if howlist is not None:
                howlist.append(val)
                return howlist
        return howlist


print("\nhowsume method 2")    
print(howsummethod2(7, [5,3,4,7]))
print(howsummethod2(7, [2,4]))
print(howsummethod2(7, [2,4,1]))
print(howsummethod2(8, [2,3,5]))


def howsummethod2MemoizeWrapper(sum, values=[]):
    memo = {}
    test = howsummethod2Memoize(sum, values, memo)
    print(memo)
    return test


def howsummethod2Memoize(sum, values=[], memo={}):
    if sum is 0:
        return []
    elif sum < 0:
        return None
    elif sum in memo:
        return memo[sum]
    else:
        howlist = None
        for val in values:
            howlist = howsummethod2Memoize(sum - val, values, memo)
            memo[sum-val] = howlist
            if howlist is not None:
                return [*howlist, val]
        return howlist


print("\nhowsume method 2 memoized")    
print(howsummethod2MemoizeWrapper(7, [5,3,4,7]))
print(howsummethod2MemoizeWrapper(7, [2,4]))
print(howsummethod2MemoizeWrapper(7, [2,4,1]))
print(howsummethod2MemoizeWrapper(300, [7,14]))
print(howsummethod2MemoizeWrapper(300, [7,14,1]))


#Avoiding python default argument behavior to avoid wrting a wrapper function

def howsummethod2MemoizeNoWrapper(sum, values=[], memo=None):
    #This is just to avoid creating a wrapper function
    if memo is None:
        memo = {}

    if sum is 0:
        return []
    elif sum < 0:
        return None
    elif sum in memo:
        return memo[sum]
    else:
        howlist = None
        for val in values:
            howlist = howsummethod2MemoizeNoWrapper(sum - val, values, memo)
            memo[sum-val] = howlist
            if howlist is not None:
                return [*howlist, val]
        return howlist


print("\nhowsume method 2 memoized without wrapper function. Trick is using 'None' as default value")    
print(howsummethod2MemoizeNoWrapper(7, [5,3,4,7]))
print(howsummethod2MemoizeNoWrapper(7, [2,4]))
print(howsummethod2MemoizeNoWrapper(7, [2,4,1]))
print(howsummethod2MemoizeNoWrapper(300, [7,14]))
print(howsummethod2MemoizeNoWrapper(300, [7,14,1]))


#complexity
'''
sum = m
number of element in array = n

Brute force 

Time Complexity -> 0(n^m *m) ( mutiplied by m because worse case there will  be 1 in array and that will return m items from an array)
Space complxity -> 0(m)


'''
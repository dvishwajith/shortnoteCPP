#!/usr/bin/env python3


def cansum(sum, values=[]):
    if sum == 0:
        return True
    elif sum < 0:
        return False
    else:
        sumpossible = False
        for val in values:
            sumpossible = cansum(sum-val, values)
            if sumpossible:
                break
        return sumpossible
    

print(cansum(7, [5,3,4,7]))
print(cansum(7, [2,4]))
print(cansum(7, [2,4,1]))
print(cansum(8, [2,3,5]))


#Wrapper function is needed becuase it seems like default {} is                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             shared between test cases
def cansumMemoizeWrapper(sum, values=[]):
    return cansumMemoize(sum, values, {})


def cansumMemoize(sum, values=[], mem={}):
    if sum == 0:
        return True
    elif sum < 0:
        return False
    elif sum in mem:
        return mem[sum]
    else:
        sumpossible = False
        for val in values:
            sumpossible = cansumMemoize(sum-val, values, mem)
            mem[sum-val] = sumpossible
            if sumpossible:
                break
        return sumpossible
    

print(cansumMemoizeWrapper(7, [5,3,4,7]))
print(cansumMemoizeWrapper(7, [2,4]))
print(cansumMemoizeWrapper(7, [2,4,1]))
print(cansumMemoizeWrapper(8, [2,3,5]))
print(cansumMemoizeWrapper(300, [7,14]))
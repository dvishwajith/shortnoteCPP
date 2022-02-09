#!/usr/bin/env python3



def quicksortwrapper(A):
    quickSort(A, 0, len(A)-1)

def quickSort(A, start, end):
    if start >= end:
        return
    pivot = getpivot(A, start, end)
    quickSort(A, start, pivot-1)
    quickSort(A, pivot+1, end)


def getpivot(A, start, end):
    pivot_value = A[end]
    moving_large_index = start # moving large index will contain the leftmost index that is going to be larger than the pivot
    i = start
    for i in range(start, end): # since "end" does not belong in range this will compare the values from index  [start, start, +1, ....., end -1]
        if A[i] < pivot_value:
            A[i], A[moving_large_index] = A[moving_large_index], A[i] # swapping min values with moving large value
            moving_large_index += 1
 
    A[moving_large_index], A[end] = A[end], A[moving_large_index] # swapping the pivot with the moving large index
    return moving_large_index # pivot index after the last swapping


test = [1,5,5,4,-3,-8,2,3,6,9,4,9,1]
# test = [5]
# test = [1,2,1,-1]
quicksortwrapper(test)
print(test)



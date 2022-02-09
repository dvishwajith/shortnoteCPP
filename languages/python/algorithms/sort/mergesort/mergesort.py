#!/usr/bin/env python3



def mergsortwrapper(A):
    mergeSort(A, 0, len(A)-1)

def mergeSort(A, start, end):
    if start == end:
        return
    mid = (end + start)//2
    mergeSort(A, start, mid)
    mergeSort(A, mid+1, end)
    merge(A, start, mid, end)

'''
Merge usign additional memory space. O(N)
'''
def merge(A, start, mid, end):
    B = A[start:end+1]
    leftedge = mid - start 
    rightedge = end - start
    i = start
    left = 0
    right = leftedge +1

    while left <= leftedge and right <= rightedge:
        if B[left] <= B[right]:
            A[i] = B[left]
            left += 1
        else:
            A[i] = B[right]
            right += 1
        i += 1

    while left <= leftedge:
        A[i] = B[left]
        left += 1
        i += 1

    while right <= rightedge:
        A[i] = B[right]
        right += 1
        i += 1

test = [2,3,6,9,4,9,1]
mergsortwrapper(test)
print(test)
"""
(If someone want to do inplace merge you will have to shift the array.
An this is an O(n^2) operation. And you can use shell sorting too.
But note that inplace merge is Hard and resaeach problem.
If someone need to do an inplace sorting use QuickSort insted of merge sort)
"""
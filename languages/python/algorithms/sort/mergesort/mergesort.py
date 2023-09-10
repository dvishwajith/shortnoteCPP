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

# seonc method

def mergsortwrapper2(A):
    mergeSort2(A, 0, len(A))

def mergeSort2(A, start, end):
    if start == end-1:
        return
    mid = (end + start)//2
    mergeSort2(A, start, mid)
    mergeSort2(A, mid, end)
    merge2(A, start, mid, end)

def merge2(A, start, mid, end):
    l = A[start:mid]
    l_index = 0
    r = A[mid:end]
    r_index = 0
    i = start

    while(l_index < (mid-start) and r_index < (end -mid)):
        if l[l_index] < r[r_index]:
            A[i] = l[l_index]
            l_index += 1
        else:
            A[i] = r[r_index]
            r_index += 1
        i += 1
    
    while(l_index < (mid-start)):
        A[i] = l[l_index]
        l_index += 1
        i += 1

    while(r_index < (end - mid)):
        A[i] = r[r_index]
        r_index += 1
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


test = [2,3,6,9,4,9,1]
mergsortwrapper2(test)
print(test)
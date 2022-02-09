#!/usr/bin/env python3

import sys

def selectionsort(A):
    for i in range(len(A)):
        minval = sys.maxsize
        for j in range(i, len(A)):
            if A[j] < minval:
                minval = A[j]
                minval_index = j
        A[i], A[minval_index] = A[minval_index], A[i] #swapping

test = [1,5,5,4,-3,-8,2,3,6,9,4,9,1]
selectionsort(test)
print(test)


def insertionSort(A):
    for i in range(len(A)):
        for j in range(i, 0, -1): #Going backward comparing
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]  #swapping

test = [1,5,5,4,-3,-8,2,3,6,9,4,9,1]
insertionSort(test)
print(test)


def BubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j] #swapping

test = [1,5,5,4,-3,-8,2,3,6,9,4,9,1]
BubbleSort(test)
print(test)
#!/usr/bin/env python3


"""
Heapify
1. Compare the children. If largest children is greater than the
parent swap that with the parent.
2. Continue heapify with the swapped child
"""
def heapify(arr, length, i):
    if (length > 2*i + 2) and (arr[2*i + 2] > arr[2*i + 1]):
        if arr[2*i + 2] > arr[i]:
            arr[2*i + 2], arr[i] = arr[i], arr[2*i + 2]
            heapify(arr, length, 2*i+2)
    else:
        if (length > 2*i+1) and (arr[2*i + 1] > arr[i]):
            arr[2*i + 1], arr[i] = arr[i], arr[2*i + 1]
            heapify(arr, length, 2*i+1)

"""
maxHeap
1. get the lowest non leaf parent indexes
2. start heapfying from lowest_parent to root.
"""
def maxHeap(arr):
    arr_len = len(arr)
    lowest_parent = (arr_len)//2
    for i in range(lowest_parent, -1, -1):
        heapify(arr, arr_len,i)

"""
HeapSort
1. Create a max heap. This is an priority queue. Contain max value in the root
2. Swap the max value with the last value. (Now and of array has the max value)
3. Heapifying from (start, last-1) ( last-1 will skip the last value , which is the max value)
4. Now root has the next max value. Swap it with (last -1) index value.
5. if we continue this we will get an array with largest value at the end and smallest value in  the front
"""
def heapsort(arr):
    arr_len = len(arr)
    maxHeap(arr)

    for i in range(arr_len -1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

test = [1,5,5,4,-3,-8,2,3,6,9,4,9,1]
# test = [5]
# test = [1,2,1,-1]
heapsort(test)
print(test)



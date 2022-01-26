#!/usr/bin/env python3
from queue import PriorityQueue
import sys

adjacencylist = [
    #u , v, Weight    
    [0, 1,  4],
    [0, 6,  7],
    [1, 6,  11],
    [1, 7,  20],
    [1, 2,  9],
    [2, 3,  6],
    [2, 4,  2],
    [3, 4,  10],
    [3, 5,  5],
    [4, 5,  15],
    [4, 7,  1],
    [4, 8,  5],
    [5, 8,  12],
    [6, 7,  1],
    [7, 8,  3]
]

'''
Another way to store weighted graphs
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
'''

def find(arr, val):
    if arr[val] == val:
        return val
    else:
        return find(arr, arr[val])

def union(arr, a, b):
    parent_a = find(arr, a)
    parent_b = find(arr, b)
    if parent_a == parent_b:
        return False
    else:
        arr[parent_b] = parent_a
        return True

def krushkal(numberofnodes, adjacencylist):
    parent_arr = [i for i in range(numberofnodes)]
    mstedges = []

    adjacencylist.sort(key = lambda x: x[2]) # sort using weight x[2]/third value is weight
    for  mincostedge in adjacencylist:
        u, v, weight = mincostedge
        if union(parent_arr, u, v):
            mstedges.append(mincostedge)
            
    return mstedges

print(" [u, v, weight] strucutre")
print(krushkal(9, adjacencylist))


def krushkalWithMstWeight(numberofnodes, adjacencylist):
    parent_arr = [i for i in range(numberofnodes)]
    mstedges = []
    mstweight = 0

    adjacencylist.sort(key = lambda x: x[2]) # sort using weight x[2]/third value is weight
    for  mincostedge in adjacencylist:
        u, v, weight = mincostedge
        if union(parent_arr, u, v):
            mstedges.append(mincostedge)
            mstweight += weight
            
    return mstedges, mstweight

print(" [u, v, weight] strucutre, MST_full_weight")
print(krushkal(9, adjacencylist))



def krushkalMethod2(numberofnodes, adjacencylist):
    parent_arr = [i for i in range(numberofnodes)]
    mstedges = []

    pq = PriorityQueue()
    for edge in adjacencylist:
        u = edge[0] # node
        v = edge[1] # node
        w = edge[2] # weight
        pq.put((w,[u,v]))

    while not pq.empty():
        weight, mincostedge = pq.get()
        if union(parent_arr, mincostedge[0],mincostedge[1]):
            mstedges.append(mincostedge)

    return mstedges

print(krushkalMethod2(9, adjacencylist))

    



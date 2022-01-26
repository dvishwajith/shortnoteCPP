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


def prims(adjacencylist):
    #constructing a graph
    graph = {}
    for edge in adjacencylist:
        u = edge[0] # node
        v = edge[1] # node
        w = edge[2] # weight
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []

        graph[u].append((v,w))
        graph[v].append((u,w))

    
    visited = set()
    pq = PriorityQueue()
    mstfullweight = 0
    # choose any randon node to start. We can star from 0
    pq.put((0,0)) # (weight=0, start=0)

    while not pq.empty():
        weight , node = pq.get()
        if node not in visited:
            mstfullweight += weight
            visited.add(node)
            for child, childweight in graph[node]:
                pq.put((childweight, child))

    return mstfullweight

print(prims(adjacencylist))






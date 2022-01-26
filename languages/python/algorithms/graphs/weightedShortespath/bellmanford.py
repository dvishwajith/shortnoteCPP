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

print(
    """
    The result will be slightly different to Dijkstras here.
    Because I am considering this Graph to be an DIrected graph. 
    In dijkstras example it was an undirected graph
    """
)

"""
Bellman ford can be applied to both directed and undirected graphs.
(In this case we re assuming this is a directed graph)
Belman Ford can detect negative weight cycles in directed graphs
Belman Ford cannot detect negative weight cycles in undirected graphs
"""

def bellmanFordDistance(adjacencylist, numberofnodes, startnode):
    #construct the graph
    graph = {}  # This can be multi dimension array too
    for link in adjacencylist:
        u = link[0]
        v = link[1]
        w = link[2]
        graph[(u, v)] = w

    dist = [sys.maxsize]*numberofnodes #dist array
    dist[startnode] = 0
    # run the edge relaxation loop for (NumberOfNodes -1) time
    for _ in range(numberofnodes-1):
        # Relax all the edges in the graph
        for edge, weight in graph.items():
            u = edge[0]
            v = edge[1]
            # if current node distance is infinity, adding to it will cause an overflow
            if dist[u] != sys.maxsize: 
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight

    #detecting negative weight cycles. In this case shortest path will not be correct
    for u, v, weight in adjacencylist:
        if dist[v] > dist[u] + weight:
            print("found negative weight cycle")        
            return                

    print("shortest distance to all the nodes ",dist)

print("\nbellmanFordDistance\n")
bellmanFordDistance(adjacencylist,9,0)

"""
Belman ford without contructing the Graph.
"""
def bellmanFordDistance2ndMethod(adjacencylist, numberofnodes, startnode):

    dist = [sys.maxsize]*numberofnodes #dist array
    dist[startnode] = 0

    # run the edge relaxation loop for (NumberOfNodes -1) time
    for _ in range(numberofnodes-1):
        # Relax all the edges in the graph
        for u, v, weight in adjacencylist:
            # if current node distance is infinity, adding to it will cause an overflow
            if dist[u] != sys.maxsize: 
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight 

    #detecting negative weight cycles. In this case shortest path will not be correct
    for u, v, weight in adjacencylist:
        if dist[v] > dist[u] + weight:
            print("found negative weight cycle")        
            return

    print("shortest distance to all the nodes ",dist)

print("\nbellmanFordDistance2ndMethod\n")   
bellmanFordDistance2ndMethod(adjacencylist,9,0)


def bellmanFordPath(adjacencylist, numberofnodes, startnode):

    dist = [sys.maxsize]*numberofnodes #dist array
    previousnode = [-1]*numberofnodes
    dist[startnode] = 0

    # run the edge relaxation loop for (NumberOfNodes -1) time
    for _ in range(numberofnodes-1):
        # Relax all the edges in the graph
        for u, v, weight in adjacencylist:
            # if current node distance is infinity, adding to it will cause an overflow
            if dist[u] != sys.maxsize: 
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    previousnode[v] = u       

    #detecting negative weight cycles. In this case shortest path will not be correct
    for u, v, weight in adjacencylist:
        if dist[v] > dist[u] + weight:
            print("found negative weight cycle")        
            return

    print("shortest distance to all the nodes ",dist)
    print("previousnode ",previousnode)

print("\nbellmanFordPath\n")
bellmanFordPath(adjacencylist,9,0)    


    

    



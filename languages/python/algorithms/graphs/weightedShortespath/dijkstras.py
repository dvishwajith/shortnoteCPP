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

def dijkstras(adjacencylist, numberofnodes, startnode):
    #construct the graph
    graph = {}  # This can be multi dimension array too
    for link in adjacencylist:
        u = link[0]
        v = link[1]
        w = link[2]
        graph[(u, v)] = w
        graph[(v, u)] = w

    dist = [sys.maxsize]*numberofnodes #dist array
    dist[startnode] = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, startnode)) #lowest weight

    while not pq.empty():
        weight, currentnode = pq.get()
        if currentnode in visited:
            continue
        visited.add(currentnode)
        for i in range(numberofnodes):
            if (currentnode,i) in graph:
                old_dist = dist[i]
                new_dist = dist[currentnode] + graph[(currentnode,i)]
                if new_dist < old_dist:
                    pq.put((new_dist, i))
                    dist[i] = new_dist
    print("shortest distance to all the nodes ",dist)
    
dijkstras(adjacencylist,9,0)
#time complexity is O(E + VlogV)                


def dijkstras2nd(adjacencylist, numberofnodes, startnode):
    #construct the graph
    graph = {}  # This can be multi dimension array too
    for link in adjacencylist:
        u = link[0]
        v = link[1]
        w = link[2]
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [sys.maxsize]*numberofnodes #dist array
    dist[startnode] = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, startnode)) #lowest weight

    while not pq.empty():
        weight, currentnode = pq.get()
        if currentnode in visited:
            continue
        visited.add(currentnode)
        for childnode, weight in graph[currentnode]:
            if dist[childnode] > dist[currentnode] + weight:
                dist[childnode] = dist[currentnode] + weight
                pq.put((dist[childnode], childnode))

    print("shortest distance to all the nodes",dist)
    print("visited ", visited)

print("\nSecond method. Graph strucutre is more elegant\n")
dijkstras2nd(adjacencylist,9,0)




def dijkstrasPath(adjacencylist, numberofnodes, startnode):
    #construct the graph
    graph = {}  # This can be multi dimension array too
    for link in adjacencylist:
        u = link[0]
        v = link[1]
        w = link[2]
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [sys.maxsize]*numberofnodes #dist array
    path = [[startnode]]*numberofnodes
    dist[startnode] = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, startnode)) #lowest weight

    while not pq.empty():
        weight, currentnode = pq.get()
        if currentnode in visited:
            continue
        visited.add(currentnode)
        currentpath = path[currentnode]
        for childnode, weight in graph[currentnode]:
            old_dist = dist[childnode]
            new_dist = dist[currentnode] + weight
            if new_dist < old_dist:
                pq.put((new_dist, childnode))
                dist[childnode] = new_dist
                # deep copy of path to current node. Otherwise child path will be
                # copied to the current path object
                child_path = list(currentpath) 
                child_path.append(childnode)
                path[childnode] = child_path

    print("shortest distance to all the nodes",dist)
    print("paths ", path)

print("""
\nPaths . We just add an additinal path list like dist for distance. 
We can stop and break after we visited the required endpoint too.
In this case we dont give an endpoint. We just find paths to all
the nodes\n
""")
dijkstrasPath(adjacencylist,9,0)


def dijkstrasPathPreviousNodeMethod(adjacencylist, numberofnodes, startnode):
    #construct the graph
    graph = {}  # This can be multi dimension array too
    for link in adjacencylist:
        u = link[0]
        v = link[1]
        w = link[2]
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [sys.maxsize]*numberofnodes #dist array
    previousNode = [-1]*numberofnodes
    dist[startnode] = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, startnode)) #lowest weight

    while not pq.empty():
        weight, currentnode = pq.get()
        if currentnode in visited:
            continue
        visited.add(currentnode)
        for childnode, weight in graph[currentnode]:
            if dist[childnode] > dist[currentnode] + weight:
                dist[childnode] = dist[currentnode] + weight
                pq.put((dist[childnode], childnode))
                previousNode[childnode] = currentnode

    print("shortest distance to all the nodes",dist)
    print("paths ", previousNode)

print("""
\ndijkstrasPathPreviousNodeMethod\n
    Just store the previous node for the shotest path in an array.
ex:- shorted path for node 8 
previousNode[8] = 7
previousNode[7] = 6
previousNode[6] = 0
previousNode[0] = -1
If it is -1 terminate. shortest path is 0, 6, 7, 8
""")
dijkstrasPathPreviousNodeMethod(adjacencylist,9,0)

    

    



#!/usr/bin/env python3

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

from collections import deque 

print("bfs first method. Using deque as a FIFO because list pop(0) is O(N)")
def BFS(graph, start):
    node_fifo = deque([])  #using  deque because pop(0) is O(N) in lists
    node_fifo.append(start)
    while len(node_fifo) != 0:
        traversed_node = node_fifo.popleft()
        print(traversed_node, " ")
        for connected_node in graph[traversed_node]:
            node_fifo.append(connected_node)

BFS(graph, 'A')


print("""bfs second method. Wihtout poping first element and using a list. 
Advantage is this store the travarsed order in nodelist as well""")
def BFS(graph, start):
    nodelist = []
    nodelist.append(start)
    for traversed_node in nodelist:
        print(traversed_node, " ")
        for connected_node in graph[traversed_node]:
            nodelist.append(connected_node)

BFS(graph, 'A')
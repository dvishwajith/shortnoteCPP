#!/usr/bin/env python3


from collections import deque


graph = {
    0 : [1,5],
    1 : [0,2],
    2 : [1,3],
    3 : [2,4],
    4 : [3,5],
    5 : [4,0],
    
}


def shortestpathcost(graph, start, end):
    visited = {}
    queue = [start]
    visited[start] = 0
    pathlen = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node == end:
            return visited[current_node]
        else:
            for child in graph[current_node]:
                if child not in visited:
                    visited[child] = visited[current_node] + 1
                    queue.append(child)


def shortestpathcost2ndmethod(graph, start, end):
    visited = set()
    queue = [(start,0)]
    visited.add(start)
    pathlen = 0
    while len(queue) > 0:
        current_node, pathlen = queue.pop(0)
        if current_node == end:
            return pathlen
        else:
            for child in graph[current_node]:
                if child not in visited:
                    queue.append((child, pathlen+1))
                    visited.add(current_node)


print(shortestpathcost(graph,0, 4))
print(shortestpathcost2ndmethod(graph,0, 4))


def shortestpath(graph, start, end):
    visited = set()
    queue = deque([])  
    # In BFS queue we are going to store paths in the FIFO, insted of visiting Nodes. 
    # So in those path , last value is the node that  we should consider as the  current node
    queue.append([start])
    visited.add(start)
    pathlen = 0
    while len(queue) > 0:
        path = queue.popleft()
        # current node is the last node of the path of the BFS queue 
        current_node = path[-1] 
        if current_node == end:
            return path
        else:
            for child in graph[current_node]:
                if child not in visited:
                    #deep copying of the path of the current node
                    copied_path = list(path)  
                    copied_path.append(child)
                    queue.append(copied_path)
                    visited.add(current_node)

print(shortestpath(graph,0, 4))
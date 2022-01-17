#!/usr/bin/env python3


graph = {
    0 : [1,5],
    1 : [0,2],
    2 : [1,3],
    3 : [2,4],
    4 : [3,5],
    5 : [4,0],
    
}


def shortestpath(graph, start, end):
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


def shortestpath2ndmethod(graph, start, end):
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


print(shortestpath(graph,0, 4))
print(shortestpath2ndmethod(graph,0, 4))


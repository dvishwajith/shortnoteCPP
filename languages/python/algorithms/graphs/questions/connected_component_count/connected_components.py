#!/usr/bin/env python3


graph = {
    0 : [8, 1, 5],
    1 : [0],
    5 : [0, 8],
    8 : [0, 5],
    2 : [3, 4],
    3 : [2, 4],
    4 : [3, 2]
}


def connecteditems(graph, start, visited):
    if start in visited:
        return
    else:
        visited.add(start)
        for child in graph[start]:
            connecteditems(graph, child, visited)

def connectedcount(graph):
    visited = set()
    components = 0
    for keynode in graph:
        if keynode not in visited:
            components += 1
            connecteditems(graph, keynode, visited)
    return components




print(connectedcount(graph))


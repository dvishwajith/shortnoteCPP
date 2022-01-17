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
        return 0
    else:
        visited.add(start)
        count = 1
        for child in graph[start]:
            count += connecteditems(graph, child, visited)
        return count

def connectedcount(graph):
    visited = set()
    maxcomponentnumber = -1
    largest_connected_graph = -1
    for keynode in graph:
        if keynode not in visited:
            numberofcomponents = connecteditems(graph, keynode, visited)
            if numberofcomponents > maxcomponentnumber:
                largest_connected_graph = keynode
                maxcomponentnumber = numberofcomponents
    return largest_connected_graph




print(connectedcount(graph))


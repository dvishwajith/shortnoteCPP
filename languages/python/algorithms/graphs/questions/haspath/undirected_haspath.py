#!/usr/bin/env python3


edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n'],
]

def covert2adjencylist(edges):
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


def haspath(graph, src , dst, visited):
    visited.add(src)
    if src == dst:
        return True
    elif src in visited:
        return False
    else:
        for child in graph[src]:
            if haspath(graph, child, dst, visited):
                return True
    return False


def undeirected_haspath(edges, src, dst):
    graph = covert2adjencylist(edges)
    visited = set()
    return haspath(graph,src, dst, visited)


print(undeirected_haspath(edges, 'm', 'n'))


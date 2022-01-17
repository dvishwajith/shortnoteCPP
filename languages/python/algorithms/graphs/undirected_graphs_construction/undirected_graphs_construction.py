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

print(covert2adjencylist(edges))
#!/usr/bin/env python3


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

node_list = []


def dfs(graph, start):
    node_list.append(start)
    while len(node_list) != 0:
        traversed_node = node_list[0]
        print(traversed_node, " ")
        del node_list[0]
        for connected_node in graph[traversed_node]:
            node_list.append(connected_node)


dfs(graph, 'A')
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
        traversed_node = node_list[-1]
        print(traversed_node, " ")
        node_list.pop()
        for connected_node in graph[traversed_node]:
            node_list.append(connected_node)


dfs(graph, 'A')


#recursive depthfirst seach

def dfs_recursive(graph, start):
    print(start, " ")
    if len(graph[start]) <= 0:
        return
    else:
        for child in graph[start]:
            dfs_recursive(graph, child)


print("Recursive dfs")
dfs_recursive(graph, 'A')

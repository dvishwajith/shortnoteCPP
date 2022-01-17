#!/usr/bin/env python3

from typing import List

def isBipartite(graph: List[List[int]]) -> bool:
    length = len(graph)
    color = [-1]*length
    qu = []
    
    for i in range(length):
        # if node is not visited start a new BFS from that node
        if color[i] == -1: 
            qu.append(i)
            color[0] = 0

        while len(qu) is not 0:
            node = qu.pop(0)
            for connected_node in graph[node]:
                if color[connected_node] != -1:
                    # False if connected node is going to be same color
                    if color[connected_node] != color[node] ^ 1: 
                        return False
                else:
                    # connected node will be , other color ( 1 if 0 , 0 if 1)
                    color[connected_node] = color[node] ^ 1 
                    qu.append(connected_node)
                                            
    return True


#input graph = [[1,3],[0,2],[1,3],[0,2]] 
#(no need of hash table since nodes are intergers and continuous)

print(isBipartite([[1,3],[0,2],[1,3],[0,2]]))
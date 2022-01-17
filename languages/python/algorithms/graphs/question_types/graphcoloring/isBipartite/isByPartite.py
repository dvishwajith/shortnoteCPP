#!/usr/bin/env python3

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        color = [-1]*length
        qu = []
        
        for i in range(length):
                if color[i] == -1: # if node is not visited start a new BFS from that node
                    qu.append(i)
                    color[0] = 0

                while len(qu) is not 0:
                    node = qu.pop(0)
                    for connected_node in graph[node]:
                        if color[connected_node] != -1:
                            if color[connected_node] != color[node] ^ 1: # False if connected node is going to be same color
                                return False
                        else:
                            color[connected_node] = color[node] ^ 1 # connected node will be , other color ( 1 if 0 , 0 if 1)
                            qu.append(connected_node)
                                             
        return True
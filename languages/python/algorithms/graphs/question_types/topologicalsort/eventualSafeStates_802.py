#!/usr/bin/env python3

#802 Eventual Safe states  Leetcode

from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        visited = [False]*length
        traversed = [False]*length
               
        safenodes = []  

        def dfs(node):
            visited[node] = True
            traversed[node] = True
            for child in graph[node]:
                if traversed[child] == True:
                    return False
                if visited[child] != True:
                    if not dfs(child):
                        return False
            traversed[node] = False
            safenodes.append(node)
            return True
                   
        for i in range(length):
            if visited[i]:
                continue
            else:
                if dfs(i):
                    pass
        return sorted(safenodes)
    
    def eventualSafeNodesBFS(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        out_connections = [0]*length
    
        bfsNoOtherInQueue = []
        graph_invert = [[] for _ in range(length)]
        for i in range(length):
            out_connections[i] = len(graph[i])
            if out_connections[i] == 0:
                bfsNoOtherInQueue.append(i)
            for outnode in graph[i]:
                graph_invert[outnode].append(i)
    
        for node in bfsNoOtherInQueue:
            for child in graph_invert[node]:
                out_connections[child] -= 1
                if out_connections[child] == 0:
                    bfsNoOtherInQueue.append(child)

        return sorted(bfsNoOtherInQueue)
               

test = Solution()
print(test.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(test.eventualSafeNodesBFS([[1,2],[2,3],[5],[0],[5],[],[]]))

#!/usr/bin/env python3

#207. Course Schedule  Leetcode
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        length = numCourses
        visited = [False]*length
        traversed = [False]*length
        graph = [[] for _ in range(length)]
        
        for edge in prerequisites:    
            graph[edge[0]].append(edge[1])
               
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
            return True
                   
          
        for i in range(length):
            if visited[i]:
                continue
            else:
                if not dfs(i):
                    return False
        return True
                
test = Solution()
print(test.canFinish(2,[[0,1]]))
print(test.canFinish(2,[[0,1], [1,0]]))

class SolutionBFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        length = numCourses
        in_connections = [0]*length
        graph = [[] for _ in range(length)]
        
        for edge in prerequisites:    
            graph[edge[0]].append(edge[1])
            in_connections[edge[1]] += 1

        bfsNoOtherInQueue = []

        inque_ref = 0
        for i in range(length):
            if in_connections[i] == 0:
                bfsNoOtherInQueue.append(i)
                inque_ref += 1

        while len(bfsNoOtherInQueue) > 0:
            node = bfsNoOtherInQueue.pop(0)
            for child in graph[node]:
                in_connections[child] -= 1
                if in_connections[child] == 0:
                    bfsNoOtherInQueue.append(child)
                    inque_ref += 1

        return inque_ref == numCourses
               

test = SolutionBFS()
print(test.canFinish(2,[[0,1]]))
print(test.canFinish(2,[[0,1], [1,0]]))
print(test.canFinish(2,[]))
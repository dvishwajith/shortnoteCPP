#!/usr/bin/env python3

from typing import List

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    parent_arr = [-1]*(len(edges)+1)
    def find(x):
        if parent_arr[x] == -1:
            return x
        return find(parent_arr[x])

    #Naive method
    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:  # x and y alread in same set
            return False  
        parent_arr[root_x] = root_y # adding root of either set/tree/chain to another
        return True

    for edge in edges:
        if not union(edge[0], edge[1]): # if both edge is already in the same set that mean this edge will cause a cycle
            return edge
    return []

#above is the naive method. Time complemxity us O(n)
#This can be optimised using 
# 1. Union by rank and  ( will optimise Union) Time complexity of find will be O(logN)
# 2. Path Compression  (Will remember preiovus root nodes) Ammortised time complexity will reach O(1)


#Naive method
#  Let there be 4 elements 0, 1, 2, 3
#  
#  Initially, all elements are single element subsets.
#  0 1 2 3 
#  
#  Do Union(0, 1)
#     1   2   3  
#    /
#   0
#  
#  Do Union(1, 2)
#       2   3   
#      /
#     1
#   /
#  0
#  
#  Do Union(2, 3)
#           3    
#          /
#        2
#       /
#     1
#   /
#  0

# 1. Union with Rank

def findRedundantConnectionOptimise1(edges: List[List[int]]) -> List[int]:
    parent_arr = [-1]*(len(edges)+1)
    rank_arr = [1]*(len(edges)+1)
    def find(x):
        if parent_arr[x] == -1:
            return x
        return find(parent_arr[x])

    #Naive method
    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:  # x and y alread in same set
            return False  

        if rank_arr[x] > rank_arr[y]:
            parent_arr[root_y] = root_x # adding root of either set/tree/chain to another
        elif rank_arr[x] < rank_arr[y]:
            parent_arr[root_x] = root_y # adding root of either set/tree/chain to another
        else:  #if rank is equal adding a child will increase Rank by one node of the parent (In here we choose parent as Y)
            parent_arr[root_x] = root_y # adding root of either set/tree/chain to another
            rank_arr[y] += 1
        return True

    for edge in edges:
        if not union(edge[0], edge[1]): # if both edge is already in the same set that mean this edge will cause a cycle
            return edge
    return []

#  
#  Let us see the above example with union by rank
#  Initially, all elements are single element subsets.
#  0 1 2 3 
#  
#  Do Union(0, 1)
#     1   2   3  
#    /
#   0
#  
#  Do Union(1, 2)
#     1    3
#   /  \
#  0    2
#  
#  Do Union(2, 3)
#      1    
#   /  |  \
#  0   2   3



# 2. Paht Compression

def findRedundantConnectionOptimise2(edges: List[List[int]]) -> List[int]:
    parent_arr = [-1]*(len(edges)+1)
    rank_arr = [1]*(len(edges)+1)

    # Path compression in Find
    def find(x):
        if parent_arr[x] == -1:
            return x
        gran_parent = find(parent_arr[x])
        parent_arr[x] = gran_parent
        return gran_parent

    #Naive method
    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:  # x and y alread in same set
            return False  

        if rank_arr[x] > rank_arr[y]:
            parent_arr[root_y] = root_x # adding root of either set/tree/chain to another
        elif rank_arr[x] < rank_arr[y]:
            parent_arr[root_x] = root_y # adding root of either set/tree/chain to another
        else:  #if rank is equal adding a child will increase Rank by one node of the parent (In here we choose parent as Y)
            parent_arr[root_x] = root_y # adding root of either set/tree/chain to another
            rank_arr[y] += 1
        return True

    for edge in edges:
        if not union(edge[0], edge[1]): # if both edge is already in the same set that mean this edge will cause a cycle
            return edge
    return []


#Let the subset {0, 1, .. 9} be represented as below and find() is called
#for element 3.
#             9
#         /   |   \  
#        4    5    6
#       /         /  \
#      0         7    8
#     /        
#    3
#   / \         
#  1   2
#When find() is called for 3, we traverse up and find 9 as representative
#of this subset. With path compression, we also make 3 and 0 as the child of 9 so 
#that when find() is called next time for 0, 1, 2 or 3, the path to root is reduced.
#
#        --------9-------
#      /   /    /  \      \
#     0   4    5    6       3 
#                  /  \    /  \
#                 7    8   1   2
#

print(findRedundantConnection(edges=[[0,1], [1,2], [0,2]]))
print(findRedundantConnectionOptimise1(edges=[[0,1], [1,2], [0,2]]))
print(findRedundantConnectionOptimise2(edges=[[0,1], [1,2], [0,2]]))
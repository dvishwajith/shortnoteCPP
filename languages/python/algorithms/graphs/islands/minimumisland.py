#!/usr/bin/env python3
import pprint
import sys
# 0 water , 1 land

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0],
]


def dfs_len(grid, i,j, ROWS,COLS, visited):
    if i < 0 or j < 0 or i >= ROWS or j >= COLS:
        return 0
    elif visited[i][j] == True:
        return 0
    elif grid[i][j] != 1:
        return 0
    else:
        visited[i][j] = True
        length = 1
        return (length 
        + dfs_len(grid, i-1,j  ,ROWS,COLS, visited)
        + dfs_len(grid, i+1,j  ,ROWS,COLS, visited)
        + dfs_len(grid, i  ,j-1,ROWS,COLS, visited)
        + dfs_len(grid, i  ,j+1,ROWS,COLS, visited))




def islandcount(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    # You can create a visited set and save memory insted of using full 2D array too,
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    minlength = sys.maxsize
    for i in range(ROWS):
        for j in range(COLS):
            if visited[i][j] != True and (grid[i][j] == 1):
                length = dfs_len(grid, i, j, ROWS, COLS, visited)
                minlength = min(minlength,length)
                pprint.pprint(visited)
    return minlength

print(grid)

print(islandcount(grid))
            



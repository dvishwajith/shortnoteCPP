#!/usr/bin/env python3
import pprint

# 0 water , 1 land

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0],
]


def dfs(grid, i,j, ROWS,COLS, visited):
    if i < 0 or j < 0 or i >= ROWS or j >= COLS:
        return
    elif visited[i][j] == True:
        return
    elif grid[i][j] != 1:
        return
    else:
        visited[i][j] = True
        dfs(grid, i-1,j  ,ROWS,COLS, visited)
        dfs(grid, i+1,j  ,ROWS,COLS, visited)
        dfs(grid, i  ,j-1,ROWS,COLS, visited)
        dfs(grid, i  ,j+1,ROWS,COLS, visited)




def islandcount(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    # You can create a visited set and save memory insted of using full 2D array too,
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    islandcount = 0
    for i in range(ROWS):
        for j in range(COLS):
            if visited[i][j] != True and (grid[i][j] == 1):
                islandcount += 1
                dfs(grid, i, j, ROWS, COLS, visited)
                pprint.pprint(visited)
    return islandcount

print(grid)

print(islandcount(grid))
            



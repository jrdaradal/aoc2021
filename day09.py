# 2021 Advent of Code Day 09 Solution
# John Roy Daradal 

# SolutionA: 575

from utils import * 

def input09(full: bool) -> list[list[int]]:
    return [[int(x) for x in line] for line in readLines(getPath(9, full))]

def day09A():
    full = True 
    grid = input09(full)
    total = 0
    for row,line in enumerate(grid):
        for col,curr in enumerate(line):
            cross = surrounding(grid, (row,col))
            if all(x > curr for x in cross):
                total += curr+1
    print(total)

def surrounding(grid: list[list[int]], center: coords) -> list[int]:
    cross: list[int] = []
    bounds = gridBounds(grid)
    row,col = center
    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        y, x = row+dy, col+dx 
        c = (y,x)
        if isInsideBounds(c, bounds):
            cross.append(grid[y][x])
    return cross


if __name__ == '__main__':
    day09A()
# 2021 Advent of Code Day 09 Solution
# John Roy Daradal 

# SolutionA: 575
# SolutionB: 1019700

from utils import * 

def input09(full: bool) -> list[list[int]]:
    return [[int(x) for x in line] for line in readLines(getPath(9, full))]

def day09A():
    full = True 
    grid = input09(full)
    low = findLowPoints(grid)
    total = sum(x[1] for x in low) + len(low)
    print(total)

def day09B():
    full = True 
    grid = input09(full)
    low = findLowPoints(grid)
    basins: list[int] = []
    for center,_ in low:
        basins.append(basinSize(grid, center))
    basins.sort(reverse=True)
    b1,b2,b3 = basins[0:3]
    print(b1*b2*b3)

def surrounding(grid: list[list[int]], center: coords) -> list[tuple[coords,int]]:
    cross: list[tuple[coords,int]] = []
    bounds = gridBounds(grid)
    row,col = center
    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        y, x = row+dy, col+dx 
        c = (y,x)
        if isInsideBounds(c, bounds):
            v = grid[y][x]
            cross.append((c,v))
    return cross

def findLowPoints(grid: list[list[int]]) -> list[tuple[coords,int]]:
    low: list[tuple[coords,int]] = []
    for row, line in enumerate(grid):
        for col,curr in enumerate(line):
            c = (row,col)
            cross = surrounding(grid, c)
            if all(x > curr for _,x in cross):
                low.append((c,curr))
    return low

def basinSize(grid: list[list[int]], center: coords) -> int:
    visited: set[coords] = set([])
    queue: list[coords] = [center]
    while len(queue) > 0:
        c = queue.pop()
        visited.add(c)
        for nc,nv in surrounding(grid, c):
            if nc not in visited and nv != 9:
                queue.append(nc)
    return len(visited)

if __name__ == '__main__':
    # day09A()
    day09B()
# 2021 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 5294
# SolutionB: 21698

from utils import * 

line = tuple[coords,coords]

def input05(full: bool) -> tuple[list[line], coords]:
    maxX, maxY = 0, 0
    lines: list[line] = []
    for text in readLines(getPath(5, full)):
        p = [x.strip() for x in text.split('->')]
        x1,y1 = [int(x) for x in p[0].split(',')]
        x2,y2 = [int(x) for x in p[1].split(',')]
        maxX = max(maxX, x1, x2)
        maxY = max(maxY, y1, y2)
        l = ((x1,y1),(x2,y2))
        lines.append(l)
    return (lines, (maxX+1,maxY+1))

def day05A():
    full = True 
    lines, (numCols,numRows) = input05(full)
    grid: list[list[int]] = [[0 for _ in range(numCols)] for _ in range(numRows)]
    for (x1,y1),(x2,y2) in lines:
        if x1 == x2:
            addVerticalLine(grid, y1, y2, x1)
        elif y1 == y2:
            addHorizontalLine(grid, x1, x2, y1)
    countGrid(grid)

def day05B():
    full = True 
    lines, (numCols, numRows) = input05(full)
    grid: list[list[int]] = [[0 for _ in range(numCols)] for _ in range(numRows)]
    for (x1,y1),(x2,y2) in lines:
        dy, dx = abs(y1-y2), abs(x1-x2)
        if x1 == x2:
            addVerticalLine(grid, y1, y2, x1)
        elif y1 == y2:
            addHorizontalLine(grid, x1, x2, y1)
        elif dy == dx:
            addDiagonalLine(grid, x1, y1, x2, y2)
    countGrid(grid)
    
def countGrid(grid: list[list[int]]):
    count = 0
    numRows, numCols = len(grid), len(grid[0])
    for y in range(numRows):
        for x in range(numCols):
            if grid[y][x] > 1:
                count += 1
    print(count)

def addVerticalLine(grid: list[list[int]], y1: int, y2: int, x: int):
    y1, y2 = sorted([y1, y2])
    for y in range(y1,y2+1):
        grid[y][x] += 1

def addHorizontalLine(grid: list[list[int]], x1: int, x2: int, y: int):
    x1, x2 = sorted([x1, x2])
    for x in range(x1, x2+1):
        grid[y][x] += 1

def addDiagonalLine(grid: list[list[int]], x1: int, y1: int, x2: int, y2:int):
    if x1 < x2:
        xRange = list(range(x1,x2+1))
    else:
        xRange = list(range(x1,x2-1,-1))
    if y1 < y2:
        yRange = list(range(y1,y2+1))
    else:
        yRange = list(range(y1,y2-1,-1))
    for i in range(len(xRange)):
        y, x = yRange[i], xRange[i]
        grid[y][x] += 1

if __name__ == '__main__':
    # day05A()
    day05B()
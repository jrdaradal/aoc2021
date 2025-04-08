# 2021 Advent of Code Day 03 Solution
# John Roy Daradal 

# SolutionA: 2261546
# SolutionB: 6775520

from utils import * 

def input03(full: bool) -> list[str]:
    return readLines(getPath(3, full))

def day03A():
    full = True 
    lines = input03(full)
    count: dict[int,int] = {}
    for line in lines:
        for i,bit in enumerate(line):
            if bit == '1':
                count.setdefault(i, 0)
                count[i] += 1
    n, mid = len(lines[0]), len(lines)/2
    g, e = [], []
    for i in range(n):
        if count[i] > mid:
            g.append('1')
            e.append('0')
        else:
            g.append('0')
            e.append('1')

    g = int(''.join(g), 2)
    e = int(''.join(e), 2)
    print(g*e)

def day03B():
    full = True 
    lines = input03(full)
    r1 = filterMax(lines)
    r2 = filterMin(lines)
    print(r1*r2)

def filterMax(lines: list[str]) -> int:
    n = len(lines[0])
    for i in range(n):
        maxBit = '0'
        c1 = countIndex(lines, i)
        c0 = len(lines) - c1 
        if c1 >= c0:
            maxBit = '1'
        lines = [line for line in lines if line[i] == maxBit]
        if len(lines) == 1:
            break
    return int(lines[0], 2)

def filterMin(lines: list[str]) -> int:
    n = len(lines[0])
    for i in range(n):
        minBit = '1'
        c1 = countIndex(lines, i)
        c0 = len(lines) - c1 
        if c0 <= c1:
            minBit = '0'
        lines = [line for line in lines if line[i] == minBit]
        if len(lines) == 1:
            break
    return int(lines[0], 2)

def countIndex(lines: list[str], index: int) -> int:
    return sum(1 for line in lines if line[index] == '1')


if __name__ == '__main__':
    day03A()
    day03B()
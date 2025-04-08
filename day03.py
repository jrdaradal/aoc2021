# 2021 Advent of Code Day 03 Solution
# John Roy Daradal 

# SolutionA: 2261546

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

if __name__ == '__main__':
    day03A()
# 2021 Advent of Code Day 02 Solution
# John Roy Daradal 

# SolutionA: 1484118


from utils import *

pair = tuple[int,int]

def input02(full: bool) -> list[pair]:
    mask = {"forward": 0, "up": -1, "down": 1}
    def convert(line: str) -> pair:
        p = line.split()
        return (mask[p[0]], int(p[1]))
    return [convert(line) for line in readLines(getPath(2, full))]

def day02A():
    full = True 
    x, y = 0, 0 
    for dy, d in input02(full):
        if dy == 0:
            x += d 
        else: 
            y += (dy * d)
    print(x*y)

if __name__ == '__main__':
    day02A()
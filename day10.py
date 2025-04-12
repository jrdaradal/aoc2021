# 2021 Advent of Code Day 10 Solution
# John Roy Daradal 

# SolutionA: 290691

from utils import * 

closer: dict[str,tuple[str,int]] = {
    ')' : ('(', 3),
    ']' : ('[', 57),
    '}' : ('{', 1197),
    '>' : ('<', 25137),
}

def input10(full: bool) -> list[str]:
    return readLines(getPath(10, full))

def day10A():
    full = True 
    total = 0 
    for line in input10(full):
        illegal = findIllegal(line)
        if illegal is not None:
            total += closer[illegal][1]
    print(total)

def findIllegal(line: str) -> str|None: 
    stack: list[str] = []
    for x in line:
        if x in closer:
            y = stack.pop()
            if y != closer[x][0]:
                return x
        else:
            stack.append(x)
    return None 

if __name__ == '__main__':
    day10A()
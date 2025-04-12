# 2021 Advent of Code Day 10 Solution
# John Roy Daradal 

# SolutionA: 290691
# SolutionB: 2768166558

from utils import * 

closer: dict[str,str] = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<',
}

opener: dict[str,str] = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>',
}

def input10(full: bool) -> list[str]:
    return readLines(getPath(10, full))

def day10A():
    full = True 
    score = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137,
    }
    total = 0 
    for line in input10(full):
        illegal = findIllegal(line)
        if illegal != None:
            total += score[illegal]
    print(total)

def day10B():
    full = True 
    score = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4,
    }
    scores = []
    for line in input10(full):
        incomplete = findIncomplete(line)
        if incomplete != None:
            s = computeScore(incomplete, score)
            scores.append(s)
    scores.sort()
    mid = len(scores) // 2 
    print(scores[mid])

def findIllegal(line: str) -> str|None: 
    stack: list[str] = []
    for x in line:
        if x in closer:
            y = stack.pop()
            if y != closer[x]:
                return x
        else:
            stack.append(x)
    return None 

def findIncomplete(line: str) -> str|None:
    stack: list[str] = []
    for x in line:
        if x in closer:
            y = stack.pop()
            if y != closer[x]:
                return None
        else:
            stack.append(x)
    
    mirror = [opener[x] for x in reversed(stack)]
    return ''.join(mirror)

def computeScore(text: str, score: dict[str,int]) -> int:
    total = 0 
    for x in text:
        total = (total * 5) + score[x]
    return total

if __name__ == '__main__':
    # day10A()
    day10B()
# 2021 Advent of Code Day 08 Solution
# John Roy Daradal 

# SolutionA: 375

from utils import * 

data = tuple[list[str],list[str]] # digits, output

def input08(full: bool) -> list[data]:
    def convert(line: str) -> data:
        a,b = [x.strip() for x in line.split('|')]
        return (a.split(), b.split())
    return [convert(x) for x in readLines(getPath(8, full))]

def day08A():
    full = True
    total = 0
    valid = (2,3,4,7) 
    for _, output in input08(full):
        count = sum(1 for x in output if len(x) in valid)
        total += count 
    print(total)

if __name__ == '__main__':
    day08A()
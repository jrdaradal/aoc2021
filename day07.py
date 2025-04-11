# 2021 Advent of Code Day 07 Solution
# John Roy Daradal 

# SolutionA: 345197
# SolutionB: 96361606

from utils import * 

def input07(full: bool) -> list[int]:
    line = readLines(getPath(7, full))
    return [int(x) for x in line[0].split(',')]

def day07A():
    full = True 
    numbers = input07(full)
    numbers.sort()
    median = numbers[len(numbers)//2]
    total = sum(abs(median-x) for x in numbers)
    print(total)

def day07B():
    full = True 
    numbers = input07(full)
    start, end = min(numbers), max(numbers)
    minCost = float('inf')
    for target in range(start,end+1):
        total = sum(sumRange(abs(target-x)) for x in numbers)
        minCost = min(minCost, total)
    print(minCost)

def sumRange(x: int) -> int:
    return sum(range(x+1))

if __name__ == '__main__':
    day07A()
    day07B()
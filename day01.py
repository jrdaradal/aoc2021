# 2021 Advent of Code Day 01 Solution
# John Roy Daradal 

# SolutionA: 1521 
# SolutionB: 1543

from utils import *

def input01(full: bool) -> list[int]:
    return [int(x) for x in readLines(getPath(1, full))]

def day01A():
    full = True 
    numbers = input01(full)
    prev = numbers[0]
    count = 0 
    for curr in numbers[1:]:
        if curr > prev:
            count += 1 
        prev = curr 
    print(count)

def day01B():
    full = True 
    numbers = input01(full)
    prev = sum(numbers[0:3])
    count = 0
    for i in range(3, len(numbers)):
        curr = sum(numbers[i-2:i+1])
        if curr > prev:
            count += 1
        prev = curr 
    print(count)

if __name__ == '__main__':
    day01A()
    day01B()
    
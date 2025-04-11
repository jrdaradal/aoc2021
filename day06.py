# 2021 Advent of Code Day 06 Solution
# John Roy Daradal 

# SolutionA: 391671
# SolutionB: 1754000560399

from utils import * 

def input06(full: bool) -> list[int]:
    line = readLines(getPath(6, full))
    return [int(x) for x in line[0].split(',')]

def day06A():
    full = True 
    fish = input06(full)
    simulate(fish, 80)

def day06B():
    full = True 
    fish = input06(full)
    simulate(fish, 256)

def simulate(fish: list[int], days: int):
    groups = {}
    for x in fish:
        groups.setdefault(x, 0)
        groups[x] += 1
        
    for _ in range(days):
        groups2 = {}
        for timer,count in groups.items():
            if timer == 0:
                timer = 6
                groups2[8] = count
            else:
                timer -= 1
            groups2.setdefault(timer, 0)
            groups2[timer] += count
        groups = groups2
    print(sum(groups.values()))

if __name__ == '__main__':
    day06A()
    day06B()
# 2021 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 22680

from utils import * 

class Bingo:
    def __init__(self, card: list[list[int]]):
        self.card = card
        self.numRows = len(card)
        self.numCols = len(card[0])
        self.mark = [[False for x in line] for line in card]
    
    def markNumber(self, number: int):
        for row,line in enumerate(self.card):
            for col,x in enumerate(line):
                if x == number:
                    self.mark[row][col] = True 
    
    @property
    def hasWon(self) -> bool:
        for row in range(self.numRows):
            if all(self.mark[row]):
                return True 
        for col in range(self.numCols):
            if all(self.mark[row][col] for row in range(self.numRows)):
                return True
        return False
    
    @property
    def score(self) -> int:
        total = 0 
        for row in range(self.numRows):
            for col in range(self.numCols):
                if not self.mark[row][col]:
                    total += self.card[row][col]
        return total

def input04(full: bool) -> tuple[list[int], list[Bingo]]:
    lines = readLines(getPath(4, full))
    numbers = [int(x) for x in lines[0].split(',')]
    cards: list[Bingo] = []
    card: list[list[int]] = []
    for line in lines[2:]:
        if line == '':
            cards.append(Bingo(card))
            card = []
        else: 
            card.append([int(x) for x in line.split()])
    cards.append(Bingo(card))
    return numbers, cards

def day04A():
    full = True 
    numbers, cards = input04(full)
    for number in numbers:
        for b in cards:
            b.markNumber(number)
            if b.hasWon:
                score = number * b.score
                print(score)
                return


if __name__ == '__main__':
    day04A()
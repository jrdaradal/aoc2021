# 2021 Advent of Code Day 08 Solution
# John Roy Daradal 

# SolutionA: 375
# SolutionB: 1019355

from utils import * 

data = tuple[list[str],list[str]] # digits, output
candidates = dict[int,list[str]]

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

def day08B():
    full = True
    original = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'.split()
    m = createMap(original)
    origClues = getClues(original)
    total = 0
    for digits, output in input08(full):
        clues = getClues(digits)
        t = alignClues(origClues, clues)
        o = translateOutput(output, t, m)
        total += int(o)
    print(total)

def getClues(digits: list[str]) -> tuple[candidates, candidates]:
    freq: dict[str,int] = {}
    size: dict[str,int] = {}
    for d in digits:
        d = sortString(d)
        size[d] = len(d)
        for x in d:
            freq.setdefault(x, 0)
            freq[x] += 1 
    count: candidates = {}
    length: candidates = {}
    for k,v in freq.items():
        count.setdefault(v, [])
        count[v].append(k)
    for k,v in size.items():
        length.setdefault(v, [])
        length[v].append(k)
    return (count, length)

def alignClues(clues1: tuple[candidates,candidates], clues2: tuple[candidates, candidates]) -> dict[str,str]:
    (count1, length1), (count2, length2) = clues1, clues2 
    t: dict[str,str] = {}
    domain: dict[str,list[str]] = {}
    for k, items2 in count2.items():
        items1 = count1[k]
        if len(items1) == 1 and len(items2) == 1:
            s1, s2 = items1[0], items2[0]
            t[s2] = s1 
        else:
            for s in items2:
                domain[s] = items1[:]

    for k in [2,3,4]:
        code = length2[k][0]
        choices = set(length1[k][0])
        unmapped = set(code)
        while len(choices) > 1:
            for c in code:
                if c in t:
                    unmapped.remove(c)
                    choices.remove(t[c])
        if len(choices) == 1:
            b, a = list(unmapped)[0], list(choices)[0]
            t, domain = assign(b, a, t, domain)

    return t

def assign(b: str, a: str, t: dict[str,str], domain: dict[str,list[str]]) -> tuple[dict[str,str],dict[str,list[str]]]:
    t[b] = a 
    if b in domain:
        del domain[b]

    sure: list[tuple[str,str]] = []
    domain2: dict[str,list[str]] = {}

    for k,items in domain.items():
        if a in items:
            items.remove(a)
        if len(items) == 1:
            sure.append((k, items[0]))
        else:
            domain2[k] = items 
    
    for (b,a) in sure:
        t, domain2 = assign(b,a,t,domain2)
        
    return (t, domain2)

def sortString(text: str) -> str:
    return ''.join(sorted(text))

def createMap(digits: list[str]) -> dict[str,str]:
    m: dict[str,str] = {}
    for i,code in enumerate(digits):
        m[code] = str(i)
    return m

def translateOutput(output: list[str], t: dict[str,str], m: dict[str,str]) -> str:
    orig: list[str] = []
    for code in output:
        out: list[str] = []
        for x in code:
            out.append(t[x])
        orig.append(''.join(sorted(out)))

    digit: list[str] = []
    for code in orig:
        digit.append(m[code])
    return ''.join(digit) 


if __name__ == '__main__':
    # day08A()
    day08B()
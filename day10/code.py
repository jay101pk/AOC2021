from os import getrandom
from typing import List

matchMap = {'(':')', ')':'(', '[':']', ']':'[', '{':'}', '}':'{', '<':'>', '>':'<'}
charMap = {'(':0, ')':0, '[':1, ']':1, '{':2, '}':2, '<':3,'>':3}
pointMap = {0:3, 1:57, 2:1197, 3:25137}


def isOpen(c : str):
    return 1 if c in ['[', '(', '{', '<'] else -1

def getRemain(l : list[str]) -> list[str]:
    c : list[str]= []
    for char in l[:-1]:
        add = isOpen(char)
        if add == -1:
            if c[-1] != char:
                raise ValueError(char)
            else:
                c.pop()
        else:
            c.append(matchMap[char])
    return c


def part1(lines: list[str]) -> list[list[str]]:
    remain : list[list[str]] = []
    sum = 0
    inc = 0
    cor = 0
    for (i,line) in enumerate(lines):
        try:
            remain.append(getRemain(line))
            inc = inc + 1
        except ValueError as e:
            sum = sum + pointMap[charMap[e.args[0]]]
            cor = cor + 1
    print(sum, cor, inc)
    return remain

def part2(incomp: list[list[str]]) -> list[int]:
    scores : list[int] = []
    for line in incomp:
        score = 0
        copy = line.copy()
        copy.reverse()
        print(line, copy)
        for c in copy:
            score = score * 5
            score = score + charMap[c] + 1
        scores.append(score)
        
    
    s = sorted(scores)
    print(s)
    print(s[24])




file = open("input.txt", "r")
lines = file.readlines()

incomp = part1(lines)
part2(incomp)
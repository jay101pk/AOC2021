import enum
from os import supports_effective_ids
import re

segMap = {2:1, 4:4,  3:7, 7:8}

file = open("input.txt", "r")
lines = file.readlines()


parts = [ y.strip().split(" ") for y in lines]
rows = [(list(map(lambda y: frozenset(y),x[:x.index("|")])),list(map(lambda y :frozenset(y) ,x[x.index("|")+1:]))) for x in parts ]

o = []

for row in rows:
    inputs = row[0]
    outputs = row[1]

    a = [segMap[len(x)] if len(x) in segMap else -1 for x in inputs ]

    one = a.index(1)
    four = a.index(4)
    eight = a.index(8)
    seven = a.index(7)
    
    for (index, s) in enumerate(inputs):
        if a[index] == -1:
            if len(s) == 5:
                if s > inputs[one]:
                    a[index] = 3
                elif len(s & inputs[four]) == 3:
                    a[index] = 5
                else:
                    a[index] = 2
            else:
                if s > inputs[four]:
                    a[index] = 9
                elif s > inputs[one]:
                    a[index] = 0
                else:
                    a[index] = 6 

    o.append([a[inputs.index(output)] for output in outputs ])

print(sum([int("".join([str(y) for y in x])) for x in o]))

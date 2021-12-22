from dataclasses import dataclass
from os import name
import re

@dataclass
class Cave:
    name: str
    big: bool
    connections: dict[str, 'Cave']


caves: dict[str, Cave] = {}


def travel(cave: Cave, traveled: list[str]) -> int:
    if cave.name == "end":
        return 1
    traveled.append(cave.name)

    count = 0
    for c, nCave in cave.connections.items():
        if c not in traveled or nCave.big:
            count += travel(nCave, traveled.copy())

    return count


def travel2(cave: Cave, traveled: list[str], double: bool) -> int:
    if cave.name == "end":
        return 1
    if cave.name == "start":
        return 0

    if cave.name in traveled:
        if not cave.big:
            double = False
    else:
        traveled.append(cave.name)

    count = 0
    for c, nCave in cave.connections.items():
        if nCave.big or c not in traveled or double:
            count += travel2(nCave, traveled.copy(), double)

    return count


with open("input.txt", "r") as file:
    for row in file:
        o = re.match(r'(\w+)-(\w+)\n', row)
        cave1 = o.group(1)
        cave2 = o.group(2)
        if cave1 in caves:
            c1 = caves[cave1]
        else:
            c1 = Cave(cave1, str.isupper(cave1), {})
            caves[cave1] = c1
        if cave2 in caves:
            c2 = caves[cave2]
        else:
            c2 = Cave(cave2, str.isupper(cave2), {})
            caves[cave2] = c2

        if cave2 not in c1.connections:
            c1.connections[cave2] = c2

        if cave1 not in c2.connections:
            c2.connections[cave1] = c1

sum = 0
for c, cave in caves['start'].connections.items():
    sum += travel(cave, ['start'])

print(sum)

sum2 = 0
for c, cave in caves['start'].connections.items():
    print(c)
    sum2 += travel2(cave, ['start'], True)

print(sum2)
import re

file = open("input", "r")
lines = file.readlines()

fishs = [int(x) for x in (re.split(r',', lines[0]))]

f = [ len(list(filter(lambda y: x == y,fishs))) for x in range(9)]

for i in range(256):
    eight = f[0]
    six = f[0]
    for j in range(1,9):
        f[j-1] = f[j]
    f[8] = eight
    f[6] = f[6] + six
print(sum(f))
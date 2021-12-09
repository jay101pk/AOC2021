import re

file = open("input", "r")
lines = file.readlines()

crabs = [int(x) for x in (re.split(r',', lines[0]))]
m = max(crabs)
cost = [0 for _ in range(m + 1)]
dis = [x for x in range(m + 1)] 

for i in range(1, m + 1):
    dis[i] = dis[i] + dis[i - 1]

for i in range(m + 1):
    c = 0
    for crab in crabs:
        c = c + dis[abs(crab - i)]
    cost[i] = c

print(min(cost))
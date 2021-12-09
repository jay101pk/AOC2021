import re

def singular(x: str):
    l = len(x)
    return l == 2 or l == 4 or l == 3 or l == 7 


file = open("input.txt", "r")
lines = file.readlines()

outputs = [re.split(r" ", x[1:]) for x in [ y.strip().split("|")[1] for y in lines  ] ]
f = filter(singular, (x  for l in outputs for x in l))
num = len(list(f))
print(num)
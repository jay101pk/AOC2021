import io
from data1 import data

numInc = 0
prev = data[0]
for i in data[1:]:
    if i > prev:
        numInc = numInc + 1
    prev = i

print(numInc)
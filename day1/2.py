import io
from data1 import data

numInc = 0
prev = data[0] + data[1] + data[2]
for i in range(1,len(data)-2):
    sum = data[i] + data[i+1] + data[i+2]
    if sum > prev:
        numInc = numInc + 1
    prev = sum

print(numInc)
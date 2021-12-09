import math
from os import device_encoding
import re
file = open("input", "r")
lines = file.readlines()

numOfLines = len(lines)
print(numOfLines)
digits = 12
ones = [0 for x in range(digits)]
for i in lines:
    num = int(i,2)
    for j in range(digits):
        if num & 0b1 == 1:
            ones[j] = ones[j] + 1
        num = num >> 1

print(ones)
gamma = 0
beta = 0
for i in range(digits):
    if ones[digits - i - 1] > 500:
        gamma = gamma + 1
    else:
        beta  = beta + 1
    gamma = gamma << 1
    beta = beta << 1
gamma = gamma >> 1
beta = beta >> 1
print (gamma, bin(gamma),beta, bin(beta), gamma*beta)

import math
from os import device_encoding
import re

def remove(l : list, place : int, keep : int):
    l2 = l.copy()
    for i in l:
        bit = (i >> place) % 2
        if bit != keep:
            l2.remove(i)
    return l2



file = open("input", "r")
lines = file.readlines()
nums = [int(x,2) for x in lines]

numOfLines = len(lines)
digits = 12
ones = [0 for x in range(digits)]
for i in nums:
    for j in range(digits):
        if i % 2 == 1:
            ones[j] = ones[j] + 1
        i = i >> 1

uno = [1 if x > 500 else 0 for x in ones]
print(ones, "\n",uno,"\n", ones[11])
nums2 = nums.copy()

it = 11
while len(nums2) > 1:
    use1 = uno[it]
    print("length", len(nums2), "use1", use1, "it", it)
    nums2 = remove(nums2, it, use1)
    it = it - 1
print(len(nums2))
a = nums2[0]

print("part 2")
it = 11
nums2 = nums.copy()
while len(nums2) > 1:
    use1 = 0 if uno[it] == 1 else 1
    print("length", len(nums2), "use1", use1, "it", it)
    nums2 = remove(nums2, it, use1)
    it = it - 1

b = nums2[0]
print(a,b, a*b)
import io
import re
file = open("data.txt", "r")
lines = file.readlines()

depth = 0
pos = 0
aim = 0
for line in lines:
    m = re.search(r'(\w+)\s(\d+)', line)
    if m.group(1) == "forward":
       pos = pos + int(m.group(2))
       depth = int(m.group(2)) * aim + depth
    elif m.group(1) == "down":
        aim = aim + int(m.group(2))
    else:
        aim = aim - int(m.group(2))

print(depth * pos)

import io
import re
file = open("data.txt", "r")
lines = file.readlines()

depth = 0
pos = 0
for line in lines:
    m = re.search(r'(\w+)\s(\d+)', line)
    if m.group(1) == "forward":
       pos = pos + int(m.group(2))
    elif m.group(1) == "down":
        depth = depth + int(m.group(2))
    else:
        depth = depth - int(m.group(2))

print(depth * pos)

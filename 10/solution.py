#!/usr/bin/env python3
# https://adventofcode.com/2022/day/10

def draw(c, x):
    if (c%40-1) in (x-1,x,x+1):
        print('#', end ='')
    else:
        print('.', end ='')
    if c % 40 == 0:
        print('')

prog = []
with open('i.txt', 'r') as f:
    for line in f.readlines():
        l = line.strip().split(' ')
        if len(l) == 1:
            prog.append((l[0], None))
        else:
            prog.append((l[0], int(l[1])))
x = 1
c = 1
vals = []
pixel = 0
print(f"Part2:")
for ins, val in prog:
    if ins == 'noop':
        draw(c,x) 
        vals.append(x) 
        c += 1
    if ins == "addx":
        for _ in range(2):
            draw(c,x) 
            vals.append(x)
            c += 1
        x += val
s = 0

for n in (20, 60, 100, 140, 180, 220):
    s+=vals[n-1]*n

print(f"\nPart1: {s}")


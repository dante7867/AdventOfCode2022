#!/usr/bin/env python3
# https://adventofcode.com/2022/day/1


##### p1 #####
with open('i.txt', 'r') as f:
    cals = []
    elves = []
    for line in f.readlines():
        line = line.strip()
        if line == '':
            elves.append(sum(cals))
            cals = []
        else:
            cals.append(int(line))
    elves.append(sum(cals))

print(f'Solution 1: {max(elves)}')


##### p2 #####
print(f'Solution 2: {sum(sorted(elves, reverse= True)[:3])}')


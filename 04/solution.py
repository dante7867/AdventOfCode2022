#!/usr/bin/env python3
# https://adventofcode.com/2022/day/4


def get_set_of_zone_ids(elf_string):
    es, ee = elf_string.split('-')
    i_es, i_ee = int(es), int(ee)
    elf = set(range(i_es, i_ee+1))
    return elf
    

with open('i.txt', 'r') as f:
    pairs = []
    for line in f.readlines():
        line = line.strip()
        e1, e2 = line.split(',')
        pairs.append((get_set_of_zone_ids(e1), get_set_of_zone_ids(e2)))


##### p1 #####
p1 = 0
for p in pairs:
    if p[0].issubset(p[1]) or p[1].issubset(p[0]):
        p1 += 1
print(f'Part1: {p1}')


##### p2 #####
p2 = 0
for p in pairs:
    if not p[0].isdisjoint(p[1]):
        p2 += 1
print(f'Part2: {p2}')


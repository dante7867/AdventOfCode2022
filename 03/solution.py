#!/usr/bin/env python3
# https://adventofcode.com/2022/day/

##### p1 #####


def get_intersection_2(l1, l2):
    i = set(l1).intersection(l2)
    return next(iter(i))


with open('i.txt', 'r') as f:
    groups = []
    group = []
    intersections = []
    for line in f.readlines():
        line = line.strip()
        half = len(line)//2
        intersections.append(get_intersection_2(line[:half], line[half:]))
        
        #p2
        group.append(set(line))
        if len(group)==3:
            groups.append(group)
            group = []


def get_prio(i):
    if i.islower():
       return ord(i) - ord('a') + 1
    else:
        return ord(i) - ord('A') + 27

p1 = 0
for i in intersections:
    p1 += get_prio(i)
print(f'Part1: {p1}')


##### p2 #####


def get_intersection_3(s1, s2, s3):
    i = s1.intersection(s2).intersection(s3)
    return next(iter(i))


p2 = 0
for g in groups:
    p2 += get_prio(get_intersection_3(g[0], g[1], g[2]))
print(f'Part2: {p2}')


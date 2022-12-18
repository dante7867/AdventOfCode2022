#!/usr/bin/env python3
# https://adventofcode.com/2022/day/


import re
import numpy as np
from collections import Counter


CUBES = [] 
with open('i.txt', 'r') as f:
    x_min, x_max, y_min, y_max, z_min, z_max = 100, -100, 100, -100, 100, -100
    for line in f.readlines():
        cube = tuple(map(int,re.findall(r'-?\d+', line)))
        CUBES.append(cube)
        x_min = min(cube[0], x_min)
        y_min = min(cube[1], y_min)
        z_min = min(cube[2], z_min)
        x_max = max(cube[0], x_max)
        y_max = max(cube[1], y_max)
        z_max = max(cube[2], z_max)

print(f'X: {x_min}-{x_max}, Y: {y_min}-{y_max}, Z: {z_min}-{z_max}')
MAX = max(x_max,y_max,z_max)+1
print('MAX', MAX, '\n')

s = np.zeros((MAX, MAX, MAX))
for c in CUBES:
    x,y,z = c
    s[x][y][z] = 1

AIR = 0
ROCK = 1
WATER = 2


def get_area_in_contact_with(s, CUBES, substance):
    area = 0
    for a in range(MAX):
        for b in range(MAX):
            for c in range(MAX):
                if (a,b,c) not in CUBES:
                    continue

                if a-1 > -1:
                    if s[a-1][b][c] == substance: area += 1
                else:
                    area += 1

                if a+1 < MAX:
                    if s[a+1][b][c] == substance: area += 1
                else:
                    area += 1

                if b-1 > -1:
                    if s[a][b-1][c] == substance: area += 1
                else:
                    area += 1

                if b+1 < MAX:
                    if s[a][b+1][c] == substance: area += 1
                else:
                    area += 1

                if c-1 > -1:
                    if s[a][b][c-1] == substance: area += 1
                else:
                    area += 1

                if c+1 < MAX:
                    if s[a][b][c+1] == substance: area += 1
                else:
                    area += 1
    return area


print('p1', get_area_in_contact_with(s, CUBES, AIR))


#### p2 ####
s[0][0][0] = WATER
drops = [(0,0,0)]

while len(drops):
    x,y,z = drops.pop()
    neightbours = [(x-1,y,z), (x+1,y,z), 
            (x,y-1,z), (x, y+1,z),
            (x,y,z-1), (x, y, z+1)]
    for a, b, c in neightbours:
        if a > -1 and a < MAX and b > -1 and b < MAX and c > -1 and c < MAX:
            if s[a][b][c] == AIR:
                s[a][b][c] = WATER
                drops.append((a,b,c))
print('--flooded--')

def get_area_in_contact_with(s, CUBES, substance):
    area = 0
    for a in range(MAX):
        for b in range(MAX):
            for c in range(MAX):
                if (a,b,c) not in CUBES:
                    continue

                if a-1 > -1:
                    if s[a-1][b][c] == substance: area += 1
                else:
                    area += 1

                if a+1 < MAX:
                    if s[a+1][b][c] == substance: area += 1
                else:
                    area += 1

                if b-1 > -1:
                    if s[a][b-1][c] == substance: area += 1
                else:
                    area += 1

                if b+1 < MAX:
                    if s[a][b+1][c] == substance: area += 1
                else:
                    area += 1

                if c-1 > -1:
                    if s[a][b][c-1] == substance: area += 1
                else:
                    area += 1

                if c+1 < MAX:
                    if s[a][b][c+1] == substance: area += 1
                else:
                    area += 1
    return area

print('p2', get_area_in_contact_with(s, CUBES, WATER))

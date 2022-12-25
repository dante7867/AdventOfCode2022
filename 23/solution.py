#!/usr/bin/env python3
# https://adventofcode.com/2022/day/23


import os
from copy import deepcopy
from collections import Counter


DIR_2_POINTS_TO_CHECK = {
        'N':([-1], [-1,0,1]),
        'S':([1], [-1,0,1]),
        'W':([-1,0,1], [-1]),
        'E':([-1,0,1], [1])
        }

DIR_2_VEC = {
        'N':(-1, 0),
        'S':(1, 0),
        'W':(0,-1),
        'E':(0,1)
        }


def pm(M):
    print('-'*len(M[0]))
    print()
    for row in M:
        print(''.join(row))
    print()
    print('-'*len(M[0]))


def should_enlarge(M):
    if '#' in M[0]:
        return True
    if '#' in M[len(M)-1]:
        return 0
    
    for row in M[1:-1]:
        if row[0] == '#' or row[-1] == '#':
            return True

    return False
        

def enlarge_map(M, elves):
    new_map = []

    up = []
    for _ in range(len(M[0])+2):
        up.append('.')
    new_map.append(up)
    
    new_row = []
    for row in M:
        new_row = ['.'] + row + ['.']
        new_map.append(new_row)

    down = deepcopy(up)
    new_map.append(down)
    
    new_elves = {}
    for pos, data in elves.items():
        y, x = pos
        tar = data
        new_elves[(y+1, x+1)] = None

    return new_map, new_elves


def is_noone_around(M,y,x):
    for dy in (-1,0,1):
        for dx in (-1,0,1):
            if dx==dy==0:
                continue
            if y+dy < len(M) and y+dy > -1 and x+dx < len(M[0]) and x+dx > -1:
                if M[y+dy][x+dx]=='#':
                    return False
    return True 


def get_target(M, y, x, order):
    for letter in order:
        #print(y,x,letter)
        clear = True
        ys, xs = DIR_2_POINTS_TO_CHECK[letter] 
        for yy in ys:
            for xx in xs:
                if y+yy < len(M) and y+yy > -1 and x+xx < len(M[0]) and x+xx > -1:
                    if not M[y+yy][x+xx]=='.':
                    #print(y+yy, x+xx, 'taken')
                        clear = False
        if clear:
            dy, dx = DIR_2_VEC[letter]
            y_tar, x_tar = y + dy, x + dx
            return (y_tar, x_tar)
    return (y, x)
            

def round(M, elves, order):
    M, elves = enlarge_map(M, elves)
    c = Counter()
    # target proposals
    for e in elves:
        y, x = e
        if not is_noone_around(M, y, x):
            tar = get_target(M, y, x, order)
            c[tar]+=1
            elves[e] = tar

    #print(elves)
    moved = len([tar for tar in elves.values() if tar != None])
    #print('moved', moved)
    
    new_elves = {}
    for e, tar in elves.items():
        if c[tar]==1:
            new_elves[tar] = None
        else:
            new_elves[e] = None
    #print(c)
    #print(new_elves)

    first = order[0]
    order = order.replace(first,'') + first

    return M, new_elves, order, moved


def redraw_map(M, elves):
    SIZE = len(M)
    nM = []
    for _ in range(SIZE):
        new_row = []
        for _ in range(SIZE):
            new_row.append('.')
        nM.append(new_row)
    
    for e in elves:
        y, x = e
        #print('elf', y, x)
        nM[y][x] = '#'
        
    return nM


def get_number_of_dots(M):
    y_min, y_max = 1e9, 0
    x_min, x_max = 1e9, 0
    for y, row in enumerate(M):
        if '#' in row:
            y_min = min(y_min, y)
            y_max = max(y_max, y)
            
            first_x = row.index('#')
            last_x = len(row) - row[::-1].index('#') - 1
            x_min = min(x_min, first_x)
            x_max = max(x_max, last_x)

    return (y_max-y_min+1)*(x_max-x_min+1)-len(elves)


M=[]
with open('i.txt', 'r') as f:
    for line in f.readlines():
        M.append(list(line.strip()))

elves = {}
for y, row in enumerate(M):
    for x, sym in enumerate(row):
        if sym == '#':
            elves[(y,x)] = None

P1_ROUNDS = 10
r = 0
order = 'NSWE'
while True:
    r+=1
    print('ROUND: #', r, 'order:', order)
    M, elves, order, moved = round(M, elves, order)
   
    if moved == 0:
        print('P2:', r)
        exit()
    M = redraw_map(M, elves)
    if r==P1_ROUNDS:
        print('P1:', get_number_of_dots(M))

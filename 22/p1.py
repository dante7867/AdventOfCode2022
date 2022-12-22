#!/usr/bin/env python3
# https://adventofcode.com/2022/day/22

import re


def pad_with_spaces(line, final_length):
    pad_length = final_length - len(line)
    return line + ' '*pad_length


def pm(M):
    print('-'*len(M[0]))
    for row in M:
        print(''.join(row))
    print('-'*len(M[0]))


def draw_me(M, y, x, dv):
    sym = dir_to_symb[dv]
    M[y][x] = sym


###################################################################


M = []
with open('i.txt', 'r') as f:
    WIDTH = 0
    for line in f.readlines():
        if '.' in line or '#' in line:
            WIDTH = max(WIDTH, len(line.strip('\n')))
    f.seek(0)
    for line in f.readlines():
        line = pad_with_spaces(line.strip('\n'), WIDTH)
        M.append(list(line))

# parse instructions to form of list
INS = []
ins = ''.join(M[-1]).strip()
i = re.findall(r'([0-9]+)|([a-zA-Z]+)', ins)
for n, l in i:
    if n == '':
        INS.append(l)
    else:
        INS.append(int(n))
print('INS:', ins)

# cut footer with empty line and instructions from map
M = M[:-2]
HEIGHT = len(M[0])
print('WIDTH:', WIDTH, 'HEIGHT:', HEIGHT)

# make sure padding is ok
for i, r in enumerate(M):
    assert len(r) == WIDTH, f"len of {i} row: {len(r)} doest eq {WIDTH}"

y, x, = 0, M[0].index('.')
dv = (0, 1) # direction vector facing right
print(f'start (y, x): ({y},{x})')

dir_to_symb = {(0,1): ">", (0,-1):"<", (1,0):"v", (-1,0):"^"}
#draw_me(M,y,x,dv)
pm(M)


def turn(dv, sym):
    directions = [(0,1), #right
        (1,0), # down
        (0,-1), # left
        (-1,0)] # up
    
    i = directions.index(dv)
    if sym == 'R':
        i = (i + 1) % len(directions)
    elif sym == 'L':
        i -= 1
    return directions[i]

assert turn((0,1), 'R') == (1,0)
assert turn((0,1), 'L') == (-1,0)
assert turn((-1,0), 'L') == (0,-1)
assert turn((-1,0), 'R') == (0,1)

def step(M, y, x, dv):
    sy, sx = y, x
    dy, dx = dv
    while True:
        ny = y + dy
        nx = x + dx
       
        # fell down from map
        if ny == len(M):
            ny = 0
        # fell up from map
        if ny == -1:
            ny = len(M)-1

        # fell right 
        if nx == len(M[0]):
            nx = 0

        # fell left
        if nx == -1:
            nx = len(M[0])-1


        # hit wall
        if M[ny][nx] == '#':
            if M[y][x] == '.': 
                return y, x # stopped by a wall
            if M[y][x] == ' ':
                return sy, sx

        if M[ny][nx] == '.':
            return ny, nx
        
        y, x = ny, nx


for i in INS:
    if type(i)==int:
        for _ in range(i):
            y, x = step(M, y, x, dv)
    elif type(i)==str:
        dv = turn(dv, i)
        print(y,x,dir_to_symb[dv])


facing = {">": 0, "v": 1, "<": 2, "^":3}
print(f'final pos: ({y},{x}), direction {dir_to_symb[dv]}, direction score {facing[dir_to_symb[dv]]}') 
print('p1:', 1000*(y+1) + 4*(x+1) + facing[dir_to_symb[dv]])

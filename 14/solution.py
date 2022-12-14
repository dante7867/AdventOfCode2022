#!/usr/bin/env python3
# https://adventofcode.com/2022/day/14


import re


def print_part_of_map(M, sy, sx, ey, ex):
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            print(M[y][x], end='')
        print()


def print_map(M):
    for row in M:
        print(''.join(row))
    print()


def create_map(y_max, x_min, x_max):
    M = []
    for rows in range(0, y_max+1):
        row = []
        for cols in range(x_min, x_max+1):
            row.append('.')
        M.append(row)
    return M


with open('i.txt', 'r') as f:
    whole = f.read()

    ys = re.findall(r',\d+', whole)
    ys = [int(y.replace(',','')) for y in ys]
    y_max, y_min = max(ys), min(ys)

    xs = re.findall(r'\d+,', whole)
    xs = [int(x.replace(',','')) for x in xs]
    x_max, x_min = max(xs), min(xs)

    M = create_map(y_max, x_min, x_max)

    #p2
    depth = y_max + 2
    M2 = create_map(depth, 0, x_max+x_min)
    for i in range(len(M2[depth])):
        M2[depth][i]='#'
    
    f.seek(0)
    strokes = []
    for line in f.readlines():
        dashes = []
        pts = re.findall(r'\d+,\d+', line)
        for p in pts:
            dashes.append(list(map(int, p.split(','))))
        strokes.append(dashes)

    for dashes in strokes:     
        for idx in range(len(dashes)-1):
            sx, sy = dashes[idx]
            ex, ey = dashes[idx+1]
            
            for y in range(min(sy,ey), max(sy,ey)+1):
                for x in range(min(sx,ex), max(sx,ex)+1):
                    M[y][x-x_min] = '#'
                    M2[y][x] = '#' #p2


pour_x, pour_y = 500, 0

MOVING = 0
STOPPED = 1
FALLEN = 2
OVERFLOW = 3

def move_sand(M, start_y, start_x, y_min, x_min):
    #time.sleep(0.1)
    y, x = start_y, start_x
    status = MOVING

    if M[y][x-x_min] == 'o':
        return OVERFLOW

    while status == MOVING:

        #down
        ny, nx = y + 1, x
        if ny < 0 or ny >= len(M) or nx-x_min < 0 or nx-x_min >= len(M[0]):
            return FALLEN
        if M[ny][nx-x_min] == '.':
            y, x = ny, nx
            continue

        #down-left
        ny, nx = y + 1, x - 1
        if ny < 0 or ny >= len(M) or nx-x_min < 0 or nx-x_min >= len(M[0]):
            return FALLEN
        if M[ny][nx-x_min] == '.':
            y, x = ny, nx
            continue
        
        #down-right
        ny, nx = y + 1, x + 1
        if ny < 0 or ny >= len(M) or nx-x_min < 0 or nx-x_min >= len(M[0]):
            return FALLEN
        if M[ny][nx-x_min] == '.':
            y, x = ny, nx
            continue
        status = STOPPED

    M[y][x-x_min] = 'o'
    return status


status = None
cnt = 0
while status!=FALLEN:
    cnt += 1
    status = move_sand(M,pour_y,pour_x,0,x_min)
print('p1:', cnt-1) #last one fell to abyss

### p2 ###
status = None
cnt = 0
while status!=OVERFLOW:
    cnt += 1
    status = move_sand(M2,pour_y,pour_x,0,0)

print('p2:', cnt-1) #last one does not make it to the cave because its full 

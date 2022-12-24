#!/usr/bin/env python3
# https://adventofcode.com/2022/day/

from collections import Counter


def move_blizzards(blizzards, H, W):
    new_blizzards = []
    for b in blizzards:
        direction, y, x = b

        if direction == '<':
            x -= 1
            if x==0:
                x=W-2
        elif direction == '>':
            x += 1
            if x==(W-1):
                x=1
        elif direction == '^':
            y -= 1
            if y==0:
                y=H-2
        elif direction == 'v':
            y += 1
            if y==(H-1):
                y=1
        
        new_blizzards.append( (direction, y, x) )
    return new_blizzards


def get_next_locations(y,x,H,W):
    locs = set()
    for ny, nx in ((y-1,x), (y+1,x), (y,x-1), (y, x+1), (y,x)):
        if 0<nx<(W-1) and 0<ny<(H-1):
            locs.add((ny, nx))
        if (ny,nx)==(0,1) or (ny,nx)==(H-1,W-2):
            locs.add((ny,nx))
    return locs


def pm(M):
    print('-'*len(M[0]))
    print()
    for row in M:
        print(''.join(row))
    print()
    print('-'*len(M[0]))


def print_map(H,W, blizzards, my, mx):
    c = Counter()
    bp2dir = {}
    for d, y, x in blizzards:
        c[(y,x)] += 1
        bp2dir[(y,x)] = d

    M = []
    for y in range(H):
        row = []
        for x in range(W):
            if x==0 or y==0 or x==(W-1) or y==(H-1):
                row.append('#')
            else:
                if (y,x) in c: #drawing blizzard
                    if c[(y,x)]==1:
                        row.append(str(bp2dir[(y,x)]))
                    else:
                        row.append(str(c[(y,x)]))
                else: # drawing dot
                    row.append('.')
        M.append(row)
    #M[my][mx]='E'
    pm(M)
    
                    
def travel(start_y, start_x, tar_y, tar_x, blizzards):
    minute = 0
    positions = set([(start_y, start_x)]) # starting point
    while True:
        if (tar_y, tar_x) in positions:
            end_blizzards = move_blizzards(blizzards, H, W)
            return  minute+1, end_blizzards

        next_positions = set()
        for y, x in positions:
            next_positions.update(get_next_locations(y,x,H,W))

        next_blizzards = move_blizzards(blizzards, H, W)
        next_blizz_positions = set((y,x) for sym, y, x in next_blizzards)

        next_positions = next_positions.difference(next_blizz_positions)

        minute += 1
        positions = next_positions
        blizzards = next_blizzards


W, H = 0, 0
blizzards = []
with open('i.txt', 'r') as f:
    row = 0
    for line in f.readlines():
        line = line.strip()
        for col in range(len(line)):
            if line[col] in '<>v^':
                blizzards.append( (line[col], row, col) )
        row += 1
    W = len(line)
    H = row

print(f'WxH:{W}x{H}')

m1, blizzards = travel(0, 1, H-2, W-2, blizzards)
print('P1', m1)

# go back to start
m2, blizzards = travel(H-1, W-2, 1, 1, blizzards)

# go back to exit again
m3, blizzards = travel(0, 1, H-2, W-2, blizzards)

print('P2', m1+m2+m3)


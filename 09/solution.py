#!/usr/bin/env python3
# https://adventofcode.com/2022/day/9


from copy import deepcopy


def move_tail(H,T,M):
    dy, dx = H[0] - T[0], H[1] - T[1]
    if abs(dx) < 2 and abs(dy) < 2:
        return
    if dy > 1:
        dy = 1
    if dx > 1:
        dx = 1
    if dy < -1:
        dy = -1
    if dx < -1:
        dx = -1
    T[0] += dy
    T[1] += dx


moves = []
with open('i.txt', 'r') as f:
    for line in f.readlines():
        di, val = line.strip().split() 
        moves.append((di, int(val)))

SIZE = 1000 # safe for map to be big enough
M = []
for _ in range(SIZE):
    row = []
    for _ in range(SIZE):
        row.append('.')
    M.append(row)

H, T = [SIZE//2, SIZE//2], [SIZE//2, SIZE//2]

part_num = 0
for rope_length in (2, 10): # for part 1 and 2
    rope = []
    for _ in range(rope_length):
        rope.append(deepcopy(H))

    s = set()
    for move in moves:
        di, val = move[0], move[1]
        for _ in range(val):
            H = rope[0]
            if di=='L':
                H[1] -= 1 
            if di=='R':
                H[1] += 1
            if di=='U':
                H[0] -= 1
            if di=='D':
                H[0] += 1
            
            for i in range(len(rope)-1):
                H = rope[i]
                T = rope[i+1]
                move_tail(H,T,M)
            T = rope[-1]
            s.add(tuple(T))

    part_num += 1
    print(f'Part{part_num}: {len(s)}')


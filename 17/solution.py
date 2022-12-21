#!/usr/bin/env python3
# https://adventofcode.com/2022/day/17


def print_cave(cave):
    print('CAVE:\n')
    for r in cave:
        print(r)


def grow(CAVE,n):
    for _ in range(n):
        CAVE.insert(0, '|.......|')


def move_right(CAVE):
    new_cave = []
    for row in CAVE:
        row = row[::-1]
        new_row = ''
        for left, right in zip(row, row[1:]):
            if left in '#-|+':
                if right == '@':
                    return CAVE
                else:
                    new_row += left
            elif left == '.':
                if right == '@':
                    new_row += '@'
                else:
                    new_row += left
            elif left == '@':
                if right == '@':
                    new_row += '@'
                else:
                    new_row += '.' 
        new_row += row[-1]
        new_cave.append(new_row[::-1])
    return new_cave


def move_left(CAVE):
    new_cave = []
    for row in CAVE:
        new_row = ''
        for left, right in zip(row, row[1:]):
            if left in '#-|+':
                if right == '@':
                    return CAVE
                else:
                    new_row += left
            elif left == '.':
                if right == '@':
                    new_row += '@'
                else:
                    new_row += '.'
            elif left == '@':
                if right == '@':
                    new_row += '@'
                else:
                    new_row += '.' 
        new_row += row[-1]
        new_cave.append(new_row)
    return new_cave


def freeze(CAVE):
    new_cave = []
    for i, row in enumerate(CAVE):
        CAVE[i] = row.replace('@','#')


def move_down(CAVE):
    new_cave = []
    for down, up in zip(CAVE[::-1], CAVE[::-1][1:]):
        new_row = ''
        for idx in range(len(down)):
            if down[idx] in '-#+|':
                if up[idx] == '@':
                    freeze(CAVE)
                    return CAVE, True
                new_row += down[idx]
            elif down[idx] == '.':
                if up[idx] == '@':
                    new_row += up[idx]
                else:
                    new_row += '.'
            elif down[idx] == '@':
                new_row += up[idx]

        new_cave.append(new_row)
    if '#' in CAVE[::-1][-1]:
        new_cave.append(CAVE[::-1][-1].replace('@','.'))

    return new_cave[::-1], False 


with open('i.txt', 'r') as f:
    jet_pattern = f.readline().strip()

rocks = [['####'], ['.#.','###','.#.'], ['..#','..#', '###'], ['#','#','#','#'], ['##','##']]


new_rocks = [
        ['|..@@@@.|'],
        ['|...@...|','|..@@@..|','|...@...|'],
        ['|....@..|','|....@..|','|..@@@..|'],
        ['|..@....|','|..@....|','|..@....|','|..@....|'],
        ['|..@@...|','|..@@...|']]

P1 = 2022
P2 = 1000000000000

part = 1
for STONES_TO_FALL in (P1, P2): 
    CAVE = ['+-------+']
    height_diff = 0
    height = 0
    pattern_search = {}
    pattern_not_found = True
    stones = 0

    r = -1 
    j = -1

    while stones != STONES_TO_FALL:
        print(f'Stones: {stones}, j: {j}', end='\r')
        stones += 1

        if pattern_not_found:
            if (j, r) not in pattern_search:
                pattern_search[(j, r)] = [(stones, len(CAVE) - 1)]
            else: pattern_search[(j, r)].append((stones, len(CAVE)-1))

            if len(pattern_search[(j,r)]) > 2:
                #print(f'({j}, {r})', '->', pattern_search[(j, r)])   
                stones_fallen_and_cave_height = pattern_search[(j,r)]
                stones_diff_1 = stones_fallen_and_cave_height[1][0] - stones_fallen_and_cave_height[0][0]
                height_diff_1 = stones_fallen_and_cave_height[1][1] - stones_fallen_and_cave_height[0][1]
                stones_diff_2 = stones_fallen_and_cave_height[2][0] - stones_fallen_and_cave_height[1][0]
                height_diff_2 = stones_fallen_and_cave_height[2][1] - stones_fallen_and_cave_height[1][1]
                if stones_diff_1 == stones_diff_2 and height_diff_1 == height_diff_2: # pattern found!
                    repeats = (STONES_TO_FALL - stones_fallen_and_cave_height[1][0])//stones_diff_2
                    stones  = stones + stones_diff_2*(repeats-1)
                    height  = height_diff_2*(repeats-1)
                    pattern_not_found = False
            
        r = (r + 1) % len(rocks)
        grow(CAVE, 3)
        CAVE = new_rocks[r] + CAVE    
        
        stopped = False
        while not stopped:
            j = (j + 1) % len(jet_pattern) 
            if jet_pattern[j] == '<':
                CAVE = move_left(CAVE)
            else:
                CAVE = move_right(CAVE)
            
            CAVE, stopped = move_down(CAVE)
     
    print(f'\np{part}:', height + len(CAVE)-1) # -1 cause of floor
    part += 1

#!/usr/bin/env python3
# https://adventofcode.com/2022/day/5


from copy import deepcopy


def parse_input(file_path):
    stacks = []
    for _ in range(10): stacks.append([])
    with open(file_path, 'r') as f:
        blankMet = False
        instructions = []
        for line in f.readlines():
            if line == '\n':
                blankMet = True
                continue
            if not blankMet:
                places = [1, 5, 9, 13, 17, 21, 25, 29, 33]
                line = line.ljust(35)
                for i, p in enumerate(places):
                    if line[p] != ' ':
                        stacks[i].append(line[p])
            else:
                line = line.replace('move', '').replace('from', '').replace('to', '').strip(' \n')
                instructions.append( [int(x) for x in line.split(' ') if x != ''] )
    for i,s in enumerate(stacks):
        if len(s) != 0:
            s.pop()
            stacks[i] = s[::-1]
    return stacks, instructions


def get_string_from_stacks_tops(stacks):
    tops = [stack[-1] for stack in stacks if len(stack)>0]
    return ''.join(tops)


def p1(stacks, instructions):
    for i in instructions:
        #print(f'move {i[0]} from {i[1]} to {i[2]}')
        for _ in range(i[0]):
            stacks[i[2]-1].append(stacks[i[1]-1].pop())
    print(f'Part1: {get_string_from_stacks_tops(stacks)}')


def p2(stacks, instructions):
    for i in instructions:
        # print(f'move {i[0]} from {i[1]} to {i[2]}')
        move, fro, to = i[0], i[1], i[2]
        if move == 1:
            stacks[to-1].append(stacks[fro-1].pop())
        else:
            moved = []
            for _ in range(i[0]):
                moved.append(stacks[i[1]-1].pop())

            for e in moved[::-1]:
                stacks[to-1].append(e) 
    print(f'Part2: {get_string_from_stacks_tops(stacks)}')


if __name__ == "__main__":
    stacks, instructions = parse_input('i.txt')
    stacks_copy = deepcopy(stacks)
    p1(stacks, instructions)
    p2(stacks_copy, instructions)


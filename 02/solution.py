#!/usr/bin/env python3
# https://adventofcode.com/2022/day/2

with open('i.txt', 'r') as f:
    games = []
    for line in f.readlines():
        games.append(line.strip().split(' '))

def eval_round(me, op):
    if me=='X':
        if op == 'A': return 3
        if op == 'B': return 0
        if op == 'C': return 6
    if me=='Y':
        if op == 'A': return 6
        if op == 'B': return 3
        if op == 'C': return 0
    if me=='Z':
        if op == 'A': return 0
        if op == 'B': return 6
        if op == 'C': return 3

def get_pick_pts(me):
    pts = {'X':1, 'Y':2, 'Z': 3,
            'A':1, 'B':2, 'C': 3}
    return pts[me]

lose = {'A':'Z', 'B': 'X', 'C':'Y'}
win = {'A':'Y', 'B':'Z', 'C':'X'}


##### p1 #####
score = 0
for g in games:
    me, op = g[1], g[0]
    score += get_pick_pts(me) + eval_round(me,op)
print(f'Part 1: {score}')


##### p2 #####
def eval_cheat_round(me, op):
    if me == 'X': #lose
        return 0 + get_pick_pts(lose[op])
    if me == 'Y': #draw
        return 3 + get_pick_pts(op)
    if me == 'Z': #win
        return 6 + get_pick_pts(win[op])

score2 = 0
for g in games:
    me, op = g[1], g[0]
    score2 += eval_cheat_round(me, op) 
print(f'Part 2: {score2}')


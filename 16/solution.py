#!/usr/bin/env python3
# https://adventofcode.com/2022/day/16


from copy import deepcopy


def set_or_update_bigger(d, k, v):
    if k not in d:
        d[k] = v
    else:
        d[k] = max(v, d[k])


valves = {} 
with open('i.txt', 'r') as f:
    for line in f.readlines():
        words = line.replace(';','').replace('rate=','').replace(',','').strip().split(' ')
        valves[words[1]]= (int(words[4]), words[9:])

ways = {('AA', 'AA'): 0}
MINUTES_LEFT = 26 
for m in range(0, MINUTES_LEFT):
    d = {}
    #print('== Minute', m+1, '==')
    for k, released in ways.items():
        me, opened_valves = k

        for ov in opened_valves.split(','):
            released += valves[ov][0]

        for next_me in valves[me][1]:
            set_or_update_bigger(d, (next_me, opened_valves), released)

        if me not in opened_valves and valves[me][0] != 0:
            set_or_update_bigger(d, (me, opened_valves+','+me), released)

    ways = d
    ### for part 2 ###
    if m + 1 == 26:
        max_released_at_26 = max(ways.values())
        for k, v in ways.items():
            if v==max_released_at_26:
                best_valves_at26 = k[1]
        ways_at_26 = deepcopy(ways)
    #################
    
p1 = max(ways.values())
print(f'Part1: {p1}')

set_best_valves_at26 = set(best_valves_at26.split(',')[1:]) # 'AA' was left here only for convenience

# Let's look for the best in terms of released preassure that did not touch any valve
# from answer from part1. We can safely assume this because elephant can't open the same
# valves and it also doesn't matter who opens what. So let's just pick the best helper to
# the best result so far.
best_with_all_different_valves = 0
for k, v in ways_at_26.items():
    loc, vvs = k
    s_valves = set(vvs.split(',')[1:]) # again getting rid of 'AA'
    if set_best_valves_at26.isdisjoint(s_valves):
        best_with_all_different_valves = max(best_with_all_different_valves, v)

print(f'Part2: {best_with_all_different_valves + max_released_at_26}')

#!/usr/bin/env python3
# https://adventofcode.com/2022/day/
from copy import deepcopy
kn = {}
ukn = {}
known = {}
with open('i.txt', 'r') as f:
    for line in f.readlines():
        words = line.strip().split(' ')
        if len(words) == 2:
            kn[words[0].replace(':', '')] = int(words[1])
        else:
            ukn[words[0].replace(':', '')] = [words[1], words[2], words[3], None]

ukn['root'][1] = '==' # for p2
left_root = ukn['root'][0]
right_root = ukn['root'][2]


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!! MANUALLY ADJUSTED !!!!!!!!!!!!!!! #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# TODO implement bisection to find proper value programatically
me = 3032_671_800_000
# not_enought = 3032_671_800_000
# to much     = 3032_671_900_000 

while True:
    known = deepcopy(kn)
    unknown = deepcopy(ukn)
    known['humn'] = me
    
    while 'root' not in known:
        new_known = {} 
        for m, data in unknown.items():
            l, op, r, _ = data
            if l in known and r in known:
                to_eval = "known['"+l+"']"+op+"known['"+r+"']"
                new_known[m] = eval(to_eval)
        known = known | new_known
        for m in new_known:
            del unknown[m]

    diff = known[left_root] - known[right_root]
    print('diff', diff, end='\r')
    
    if diff < 0:
        print('left to big!', me)

    if known['root'] == 1:
        print('P2:', me)
        break
    me += 1


#!/usr/bin/env python3
# https://adventofcode.com/2022/day/

unknown = {}
known = {}
with open('i.txt', 'r') as f:
    for line in f.readlines():
        words = line.strip().split(' ')
        if len(words) == 2:
            known[words[0].replace(':', '')] = int(words[1])
        else:
            unknown[words[0].replace(':', '')] = (words[1], words[2], words[3], None)

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

print('P1', int(known['root']))

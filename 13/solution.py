#!/usr/bin/env python3
# https://adventofcode.com/2022/day/13


from functools import cmp_to_key


pairs = []
with open('i.txt', 'r') as f:
    pairs_txt = f.read().split('\n\n')
    for p in pairs_txt:
        s = p.split('\n')
        pairs.append((eval(s[0]), eval(s[1])))


def compare_lists(l,r):
    ans = 0
    for x, y in zip(l, r):
        ans = compare(x,y)
        if ans != 0:
            return ans
    if len(l) < len(r):
        return 1
    elif len(l) == len(r):
        return 0
    else:
        return -1


def compare(l, r):
    if type(l)==int and type(r)==int:
        if l < r:
            return 1
        elif l==r:
            return 0
        else:
            return -1
    if type(l)==list and type(r)==int:
        r = [r]
    if type(l)==int and type(r)==list:
        l = [l]

    return compare_lists(l, r)


packets = []
in_order = 0
idx = 0
for test in pairs:
    idx += 1
    ans = compare(test[0], test[1])

    if ans == 1:
        in_order += idx
        packets.append(test[0])
        packets.append(test[1])
    else:
        packets.append(test[1])
        packets.append(test[0])

print('p1:',in_order)


### p2 ###
searched = 1
packets.append([[2]])
packets.append([[6]])

sp = sorted(packets, key=cmp_to_key(compare), reverse=True)
for i, p in enumerate(sp):
    if p in ([[2]], [[6]]):
        
        searched *= i+1
print('p2:', searched)

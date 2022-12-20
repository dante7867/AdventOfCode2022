#!/usr/bin/env python3
# https://adventofcode.com/2022/day/20


from copy import deepcopy
from collections import deque


original = []
replaced = {}
unused  = 10_000
with open('i.txt', 'r') as f:
    for line in f.readlines():
        n = int(line.strip())
        if n not in original:
            original.append(n)
        else:
            replaced[unused] = n
            original.append(unused)
            unused += 1

assert len(original) == len(set(original))


# warning! doesnt work for p2 probably due to some off by one errors
# works for p1
def mix_v1(original, replaced, numbers):
    for i, n in enumerate(original):
        if n == 0:
            continue
        real = n
        if n in replaced:
            real = replaced[n]
        idx = numbers.index(n)
        swap_idx = idx
        for _ in range(abs(real)):
            idx = swap_idx
            if real > 0:
                swap_idx = idx + 1
                if idx + 1 == len(numbers):
                    swap_idx = 0
            if real < 0:
                swap_idx = idx - 1
                if swap_idx == -1:
                    swap_idx = len(numbers) - 1
            numbers[idx], numbers[swap_idx] = numbers[swap_idx], numbers[idx]
    return numbers


# warning! doesnt work for p2 probably due to some off by one errors
# works for p1
def mix_v2(original, replaced, numbers):
    for i, n in enumerate(original):
        if n == 0:
            continue
        real = n
        if n in replaced:
            real = replaced[n]
        src_idx = numbers.index(n)
        dst_idx = ((src_idx + real) % len(numbers) + (src_idx + real)//len(numbers)) % len(numbers)
        numbers.insert(dst_idx, numbers.pop(src_idx))
    return numbers


def mix_v3(original, replaced, numbers):
    dq = deque(numbers)
    for i,n in enumerate(original):
        if n==0:
            continue
        real = n
        if n in replaced:
            real = replaced[n]
        idx = dq.index(n)
        dq.remove(n)
        dq.rotate(-real)
        dq.insert(idx, n)
    return list(dq)


def get_grove_coords(numbers, replaced):
    zero_idx = numbers.index(0)
    s = 0
    for i in (1000, 2000, 3000):
        i = (zero_idx + i) % len(numbers)
        searched  = numbers[i]
        if searched in replaced:
            searched = replaced[searched]
        #print('searched:', searched)
        s += searched
    return s


numbers = deepcopy(original)
#print('init', original)
numbers = mix_v3(original, replaced, numbers)
print('p1', get_grove_coords(numbers, replaced))


### p2 ###

dkey = 811589153
original2 = [x*dkey for x in original]
replaced2 = {}
for k, v in replaced.items():
    replaced2[k*dkey]=v*dkey

numbers2 = deepcopy(original2)
#print('init', original2)
for m in range(10):
    print(f'Mix {m}/10')
    numbers2 = mix_v3(original2, replaced2, numbers2)
    #print(numbers2)

print('p2', get_grove_coords(numbers2, replaced2))

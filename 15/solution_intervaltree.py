#!/usr/bin/env python3
# https://adventofcode.com/2022/day/

import re, intervaltree


INPUT_FILE, Y, MIN, MAX = 'e.txt', 10, 0, 20
INPUT_FILE, Y, MIN, MAX = 'i.txt', 2000000, 0, 4_000_000


sensors = []
beacons = []
with open(INPUT_FILE, 'r') as f:
    for line in f.readlines():
        nums = list(map(int,re.findall(r'-?\d+', line)))
        man_radius = abs(nums[0]-nums[2])+abs(nums[1]-nums[3])
        sensors.append((nums[0], nums[1], man_radius))
        beacons.append((nums[2], nums[3], None))

rows = {}
cnt = 0
for s in sensors:
    x,y,r = s
    cnt += 1
    #print(f'Analyzing sensor {cnt}/{len(sensors)} ...')
    for col in range(y-r,y+r+1):
        w = abs(abs(col - y)-r)
        if col not in rows:
            rows[col] = [(x-w,x+w+1)]
        else:
            rows[col].append((x-w, x+w+1))


def get_num_of_covered_or_taken_pts(rows, Y):
    s = set()

    for start, stop in rows[Y]:
        for x in range(start, stop):
            s.add(x)
    for x,y,_ in beacons:
        if y==Y:
            if x in s:
                s.remove(x)
    return len(s)

print(f"Part1: {get_num_of_covered_or_taken_pts(rows, Y)}")


### p2 ###
for YY in range(MIN, MAX):
    tree = intervaltree.IntervalTree.from_tuples(rows[YY])
    tree.merge_overlaps(strict=False)
    if 1 != len(tree.items()):
        ends = [inter.end for inter in list(tree)]
        print(f'Checked row #{YY} of {MAX}')
        print('Part2:', YY + 4000000*min(ends))
        exit() 
    print(f'Checked row #{YY} of {MAX}', end='\r')

print('Warning! No solution for part2 found!!!')


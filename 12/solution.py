#!/usr/bin/env python3
# https://adventofcode.com/2022/day/12

from collections import defaultdict
import heapq as heap


def find_symbol(M, searched):
    for y, row in enumerate(M):
        for x, sym in enumerate(row):
            if sym == searched:
                return y, x


def find_symbols(M, searched):
    pts = []
    for y, row in enumerate(M):
        for x, sym in enumerate(row):
            if sym == searched:
                pts.append((y,x))
    return pts


def get_adj(node, M):
    y, x = node
    adj = []
    for dy,dx in [(0,-1), (0,1), (-1,0), (1,0)]:
        ny, nx =  y + dy, x + dx
        if nx < 0 or ny < 0 or ny >= len(M) or nx >= len(M[0]):
            continue
        
        cur = M[y][x]
        tar = M[ny][nx]
        if cur in 'SE':
            cur = 'a'
        if tar in 'SE':
            tar = 'z'

        if ord(cur) - ord(tar) >= -1:
            adj.append((ny, nx))

    return adj
        

def solve(M, start, end):
    visited = set()
    pq = []
    heap.heappush(pq, (0, start))
    c = {start:0}
    while pq:
        cost, node = heap.heappop(pq)
        visited.add(node)

        for adj in get_adj(node, M):
            if adj in visited: continue
            if adj == end:
                return cost+1
            if adj not in c:
                c[adj]=cost+1
                heap.heappush(pq, (cost+1, adj))
            else:
                if cost + 1 < c[adj]:
                    c[adj] = cost+1
                    heap.heappush(pq, (cost+1, adj))

### p1 ###
M = []
with open('i.txt', 'r') as f:
    for line in f.readlines():
        M.append(list(line.strip()))

start = find_symbol(M, 'S')
end = find_symbol(M, 'E')

print('p1:', solve(M,start,end))


### p2 ###
starts = find_symbols(M, 'a')
As = []
for st in starts:
    shortest = solve(M,st,end)
    As.append(shortest)
As = [x for x in As if x!=None]
print('p2:', min(As))

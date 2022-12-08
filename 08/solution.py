#!/usr/bin/env python3
# https://adventofcode.com/2022/day/


m = []
with open('i.txt', 'r') as f:
    for line in f.readlines():
        l = list(line.strip())
        m.append([int(x) for x in l])

##### p1 #####


def is_visible_vert(y,x,m):
    pt = m[y][x]
    left = m[y][:x]
    l_v = len([*filter(lambda x: x < pt, left)]) == len(left) 
    right = m[y][x+1:]
    r_v = len([*filter(lambda x: x < pt, right)]) == len(right) 
    return l_v or r_v


def is_visible_hor(y,x,m):
    col = []
    pt = m[y][x]
    for i in range(0, len(m)):
        col.append(m[i][x])
    up = col[:y]
    u_v = len([*filter(lambda x: x < pt, up)]) == len(up) 
    down = col[y+1:]
    d_v = len([*filter(lambda x: x < pt, down)]) == len(down) 
    return u_v or d_v


def is_visible(y, x, m):
    return is_visible_hor(y,x,m) or is_visible_vert(y,x,m)


def p1(m):
    v = 2*len(m) + 2*len(m[0]) - 4 # edges
    s, e = 1, len(m) - 1
    for y in range(s,e):
        for x in range(s,e):
            #print(m[y][x])
            if is_visible(y,x,m):
                v += 1
    return v


print(f'Part1: {p1(m)}')


##### p2 #####


def cnt_visible(pt,l):
    
    cnt = 0
    highest_so_far = 0 
    for i in range(len(l)):
        cnt += 1
        if l[i] >= pt:
            break
    return cnt


def cnt_up(y,x,m):
    col = []
    pt = m[y][x]
    for i in range(0, len(m)):
        col.append(m[i][x])
    up = col[:y][::-1]
    return cnt_visible(int(m[y][x]), up)


def cnt_down(y,x,m):
    col = []
    pt = m[y][x]
    for i in range(0, len(m)):
        col.append(m[i][x])
    down = col[y+1:]
    return cnt_visible(int(m[y][x]), down)


def cnt_left(y,x,m):
    left = m[y][:x][::-1]
    return cnt_visible(int(m[y][x]), left)


def cnt_right(y,x,m):
    right = m[y][x+1:]
    return cnt_visible(int(m[y][x]), right)


def cnt_scenic_score(y,x,m):
    u = cnt_up(y,x,m)
    d = cnt_down(y,x,m)
    l = cnt_left(y,x,m)
    r = cnt_right(y,x,m)
    score =  u*d*l*r
    #print(f'({y},{x})={m[y][x]} -> {u=} {d=} {l=} {r=} {score=}\n')
    return score


def p2(m): 
    highest_scenic_score = 0  
    for y in range(len(m)):
        for x in range(len(m)):
            score = cnt_scenic_score(y,x,m)
            if highest_scenic_score < score:
                highest_scenic_score = score
    return highest_scenic_score


print(f'Part2: {p2(m)}')


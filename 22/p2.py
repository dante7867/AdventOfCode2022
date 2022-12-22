#!/usr/bin/env python3
# https://adventofcode.com/2022/day/22

import re, os


# !!! WARNING !!!
# Works only for my kind of layout
#+────────+─────────+────────+
#|        | ORANGE  | GREEN  |
#+────────+─────────+────────+
#|        | BLUE    |        |
#+────────+─────────+────────+
#| RED    | PURPLE  |        |
#+────────+─────────+────────+
#| BLACK  |         |        |
#+────────+─────────+────────+
# colors for comments not to lose track of wrap teleports


def pad_with_spaces(line, final_length):
    pad_length = final_length - len(line)
    return line + ' '*pad_length


def pm(M):
    print('-'*len(M[0]))
    for row in M:
        print(''.join(row))
    print('-'*len(M[0]))


def draw_me(M, y, x, dv):
    sym = dir_to_symb[dv]
    M[y][x] = sym


###################################################################


M = []
with open('i.txt', 'r') as f:
    WIDTH = 0
    for line in f.readlines():
        if '.' in line or '#' in line:
            WIDTH = max(WIDTH, len(line.strip('\n')))
    f.seek(0)
    for line in f.readlines():
        line = pad_with_spaces(line.strip('\n'), WIDTH)
        M.append(list(line))

# parse instructions to form of list
INS = []
ins = ''.join(M[-1]).strip()
i = re.findall(r'([0-9]+)|([a-zA-Z]+)', ins)
for n, l in i:
    if n == '':
        INS.append(l)
    else:
        INS.append(int(n))

# cut footer with empty line and instructions from map
M = M[:-2]
HEIGHT = len(M[0])
print('WIDTH:', WIDTH, 'HEIGHT:', HEIGHT)


# make sure padding is ok
for i, r in enumerate(M):
    assert len(r) == WIDTH, f"len of {i} row: {len(r)} doest eq {WIDTH}"

y, x, = 0, M[0].index('.')
dv = (0, 1) # direction vector facing right

dir_to_symb = {(0,1): ">", (0,-1):"<", (1,0):"v", (-1,0):"^"}

def turn(dv, sym):
    directions = [(0,1), #right
        (1,0), # down
        (0,-1), # left
        (-1,0)] # up`
    
    i = directions.index(dv)
    if sym == 'R':
        i = (i + 1) % len(directions)
    elif sym == 'L':
        i -= 1
    return directions[i]

assert turn((0,1), 'R') == (1,0)
assert turn((0,1), 'L') == (-1,0)
assert turn((-1,0), 'L') == (0,-1)
assert turn((-1,0), 'R') == (0,1)


def step(M, y, x, dv):
    sy, sx, sdv = y, x, dv 
    
    dy, dx = dv
    
    ny = y + dy
    nx = x + dx
    ndv = dv

    sym = dir_to_symb[dv]
    # WARPING TIME
    
    ##################
    # GREEN TO BLUE #1 
    if sym == 'v' and ny==50 and 100<=nx<=149:
        ny=nx-50 
        nx=99 
        ndv=(0,-1)
        warped=True
    # BLUE TO GREEN #1
    elif sym == '>' and 50<=ny<=99 and nx==100:
        nx=ny+50 
        ny=49 
        ndv=(-1,0)
    #################
    # GREEN TO PURPLE #2
    elif sym == '>' and 0<=ny<=49 and nx==150:
        ny=(49-ny%50)+100
        nx=99
        ndv=(0,-1)
    # PURPLE TO GREEN #2
    elif sym=='>' and 100<=ny<=149 and nx==100:
        ny=49-ny%50
        nx=149
        ndv = (0,-1)
    #################
    # PURPLE TO BLACK #3
    elif sym=='v' and ny==150 and 50<=nx<=99:
        ny=nx%50+150
        nx=49
        ndv=(0,-1)
    # BLACK TO PURPLE #3
    elif sym=='>' and 150<=ny<=199 and nx==50:
        nx=50+ny%50
        ny=149
        ndv=(-1,0)
    #################
    # BLUE TO RED #4
    elif sym=='<' and 50<=ny<=99 and nx==49:
        nx=ny%50
        ny=100
        ndv=(1,0)
    # RED TO BLUE #4
    elif sym=='^' and ny==99 and 0<=nx<=49:
        ny=nx%50+50
        nx=50
        ndv=(0,1)
    #################
    # RED TO ORANGE #5
    elif sym=='<' and 100<=ny<=149 and nx == -1:
        ny=49-ny%50
        nx=50
        ndv=(0,1)
    # ORANGE TO RED #5
    elif sym=='<' and 0<=ny<=49 and nx==49:
        ny=(49-ny%50)+100
        nx=0
        ndv=(0,1)
    ################
    # BLACK TO ORANGE #6
    elif sym=='<' and 150<=ny<=199 and nx==-1:
        nx=50+(ny%50)
        ny=0
        ndv=(1,0)
        warped=True
    # ORANGE TO BLACK #6
    elif sym=='^' and ny==-1 and 50<=nx<=99:
        ny=150+(nx%50)
        nx=0
        ndv=(0,1)
    ################
    # GREEN TO BLACK #7
    elif sym=='^' and ny==-1 and 100<=nx<=149:
        nx=nx%50
        ny=199
        ndv=(-1,0)
    # BLACK TO GREEN #7
    elif sym=='v' and ny==200 and 0<=nx<=49:
        nx=nx%50+100
        ny=0
        ndv=(1,0)

    if M[ny][nx] == '#':
        assert ny>=0 and nx>=0,'stayed'
        assert M[ny][nx]!=' ','space stayed'
        ny, nx, ndv = sy, sx, sdv

    assert ny>=0 and nx>=0,'moved'
    assert M[ny][nx]!=' ','space moved'

    return ny, nx, ndv
        

for i in INS:
    if type(i)==int:
        for _ in range(i):
            y, x, dv = step(M, y, x, dv)
    elif type(i)==str:
        dv = turn(dv, i)

facing = {">": 0, "v": 1, "<": 2, "^":3}
print(f'final pos: ({y},{x}), direction {dir_to_symb[dv]}, direction score {facing[dir_to_symb[dv]]}') 
print('p2:', 1000*(y+1) + 4*(x+1) + facing[dir_to_symb[dv]])

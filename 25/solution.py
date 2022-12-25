#!/usr/bin/env python3
# https://adventofcode.com/2022/day/25


from copy import deepcopy


def snafu2decimal(snafu_num):
    decimal=0
    mult = 5**(len(snafu_num)-1)
    for snafu_symbol in snafu_num:
        digit = SNAFU_2_DIGITAL[snafu_symbol]
        decimal += mult * digit
        mult = mult//5
    return decimal


inp = []
with open('i.txt', 'r') as f:
    for line in f.readlines():
        inp.append(line.strip())

SNAFU_2_DIGITAL={'2':2,'1':1,'0':0,'-':-1,'=':-2}

s = 0
for snafu_num in inp:
    s += snafu2decimal(snafu_num)
print('sum:', s)

p = 0
while 5**p < s:
    p+=1

start = '2'*p
start = list(start)
SNAFU_SYMBOLS = ['2','1','0','-','=']
for idx in range(1, len(start)):
    cp = deepcopy(start)
    prev = 2
    for sym in SNAFU_SYMBOLS:
        cp[idx] = sym
        diff = snafu2decimal(cp) - s
        if diff < 0:
            break
        prev = sym 
    start[idx] = prev

print('P1:', ''.join(start))

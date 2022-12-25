#!/usr/bin/env python3
# https://adventofcode.com/2022/day/25

from copy import deepcopy
import itertools

inp = []
with open('i.txt', 'r') as f:
    for line in f.readlines():
        inp.append(line.strip())


sanfu_symbol2digit={'2':2,'1':1,'0':0,'-':-1,'=':-2}


def snafu2decimal(snafu_num):
    decimal=0
    mult = 5**(len(snafu_num)-1)
    for snafu_symbol in snafu_num:
        digit = sanfu_symbol2digit[snafu_symbol]
        decimal += mult * digit
        mult = mult//5
    #print(snafu_num, decimal)
    return decimal


s = 0
for snafu_num in inp:
    s += snafu2decimal(snafu_num)

print('sum', s)
TAR = s
N = ['2','1','0','-','=']
ps = deepcopy(N)
def snafu_with_len(n):
    N = ['2','1','0','-','=']
p = 0
while 5**p < s:
    p+=1
print(p, 5**p)




"""
#better
l=0
while True:
    l += 1
    print(f'considering len of number = {l}')
    for p in itertools.product(N, repeat=l):
        if snafu2decimal(p) == TAR:
            print(''.join(p))
            exit()

"""




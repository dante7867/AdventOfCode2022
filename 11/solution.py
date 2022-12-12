#!/usr/bin/env python3
# https://adventofcode.com/2022/day/11


import re, math
from copy import deepcopy


class Monkey:
    def __init__(self, idx, items, op, div, tar_true, tar_false):
        self.idx = idx
        self.items = list(map(int, items))
        self.op = op
        self.div = div
        self.tar_true = tar_true
        self.tar_false = tar_false
        self.inspections = 0
        self.old = 0


    def __repr__(self):
        return f"Monkey {self.idx}: {self.items=}"


    def play(self, monkeys,divisor,modulo):
        for i in self.items:
            old = i
            new = eval(self.op)
            
            if modulo == None: # for part1
                new = math.floor(new/divisor)
            elif divisor == None: # for part 2
                new = math.floor(new%modulo)

            tar = self.tar_true if (new % self.div == 0) else self.tar_false
            monkeys[tar].items.append(new)
            self.inspections += 1
        self.items = []
    

def p1(monkeys):
    ROUNDS = 20
    for r in range(ROUNDS):
        for m in monkeys:
            m.play(monkeys, 3, None)

    ins = sorted([m.inspections for m in monkeys])
    print(f'Part1: {ins[-1]*ins[-2]}')


def p2(monkeys):
    divs = set([m.div for m in monkeys])
    MODULO = math.prod(divs)
    ROUNDS = 10_000
    for r in range(ROUNDS):
        for m in monkeys:
            m.play(monkeys, None, MODULO)

    ins = sorted([m.inspections for m in monkeys])
    print(f'Part2: {ins[-1]*ins[-2]}')


monkeys = []
with open('i.txt', 'r') as f:
    whole = f.read()
    l_txt = whole.split('\n\n')
     
    for m in l_txt:
        l = m.split('\n')

        idx = int(re.findall(r'\d+', l[0])[0])
        items = re.findall(r'\d+', l[1])
        op = l[2].replace("Operation: ",'').replace(' ','').replace('new=','')
        div = int(re.findall(r'\d+', l[3])[0])
        tar_true =  int(re.findall(r'\d+', l[4])[0])
        tar_false =  int(re.findall(r'\d+', l[5])[0])

        monkeys.append(Monkey(idx, items, op.strip(), div, tar_true, tar_false))

monkeys_copy = deepcopy(monkeys)
p1(monkeys)
p2(monkeys_copy)


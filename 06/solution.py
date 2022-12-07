#!/usr/bin/env python3
# https://adventofcode.com/2022/day/6

with open('i.txt', 'r') as f:
    line = f.readline() 

def get_marker_position(line, header_len):
    for i, char in enumerate(line):
        if len(set(line[i:i+header_len]))==header_len:
            return i + header_len

print(f'p1: {get_marker_position(line, 4)}') 
print(f'p2: {get_marker_position(line, 14)}') 


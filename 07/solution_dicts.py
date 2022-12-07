from collections import defaultdict

with open('i.txt', 'r') as f:
    lines = f.readlines()

root = {}
current = root
dirs = []

for l in lines:
    if '$ cd' in l:
        if '..' in l:
            dirs.pop()
            current = root
            for d in dirs:
                current = current[d]
        else:
            new = l.strip().split(' ')[-1]
            current[new] = {}
            current = current[new]
            dirs.append(new)
    elif '$ ls' in l:
        pass
    elif 'dir ' in l:
        pass
    else:
        file_size, file_name = l.strip().split(' ')
        current[file_name] = int(file_size) 

        
root = root['/']

def get_rec_size(d):
    size = 0
    if not d:
        d['size'] = size
    else:
        for k,v in d.items():
            if type(v)==int:
                size += v
            else:
                size += get_rec_size(v)
        d['size'] = size
    return size
get_rec_size(root)
print(root)

SIZES = []
def get_sizes(d):
    global SIZES
    if 'size' in d:
        SIZES.append(d['size'])
    for k,v in d.items():
        if type(v)==dict:
            get_sizes(v)
get_sizes(root)
print(SIZES)

only_small = [x for x in SIZES if x <= 100000]
print(f'p1: {sum(only_small)}')

#p2
unused = 70000000 - root['size']
print(unused)
big_enough = [x for x in SIZES if x + unused >= 30000000]
print(f'p2: {min(big_enough)}')


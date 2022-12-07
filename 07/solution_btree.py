from treelib import Node, Tree

with open('i.txt', 'r') as f:
    lines = f.readlines()

tree = Tree()
cwd = tree.create_node('/','/')

lines = lines[1:]
for l in lines:
    if '$ cd' in l:
        path = l.strip().split(' ')[-1]
        if path=='..':
            cwd = tree.get_node(cwd.bpointer)
        else:
            cwd = tree.get_node(cwd.identifier + '/' + path)
    elif '$ ls' in l:
        pass
    elif 'dir' in l:
        dir_name = l.strip().split(' ')[-1]
        tree.create_node(dir_name, cwd.identifier + '/' + dir_name,  cwd, data = None)
    else:
        file_size, file_name = l.strip().split(' ')
        tree.create_node(file_name, cwd.identifier + '/' +file_name, cwd, data=int(file_size))

dirs = [tree[node].identifier for node in tree.expand_tree(filter = lambda x: x.data==None)]
dirs2size = {}

def get_size(tree, node_id):
    t = tree.subtree(node_id)
    nodes = [t[node].data for node in t.expand_tree(mode=Tree.DEPTH)]
    nodes = [x for x in nodes if x != None]
    dirs2size[node_id] = sum(nodes)

for d in dirs:
    get_size(tree, d)
AT_MOST = 100000
VALS = [x for x in dirs2size.values() if x <= AT_MOST]
print('p1:', sum(VALS))

FS_SIZE = 70000000
NEEDED = 30000000
unused = FS_SIZE - dirs2size['/']

after_del = [x for x in dirs2size.values() if x+unused >= NEEDED]
print('p2:', min(after_del))

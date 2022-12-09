import networkx as nx
f = open("2022/day_7/input.txt", "r")
text = f.read().strip()
split_text = text.split("\n")

# tree building
G = nx.DiGraph()
cd = '/'
G.add_node(cd, type='directory')
for line in split_text[1:]:
    tokens = line.split(' ')
    # cd command
    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '..':
                # print('moving to predecessor')
                cd = list(G.predecessors(cd))[0]
            else:
                # print('moving to successor')
                # node names are their complete path; it is necessary to extract 
                # the last token in their name string to make a comparison
                successors_last_token = [successor.split(
                    '/')[-1] for successor in list(G.successors(cd))]
                successor = list(G.successors(cd))[
                    successors_last_token.index(tokens[2])]
                cd = successor

    # ls command
    # ls -> directory
    elif tokens[0] == 'dir':
        G.add_edge(cd, cd + '/' + tokens[1])
        G.nodes[(cd + '/' + tokens[1])]['type'] = 'directory'

    # ls -> file
    elif tokens[0].isnumeric():
        G.add_edge(cd, cd + '/' + tokens[1])
        G.nodes[(cd + '/' + tokens[1])]['type'] = 'file'
        G.nodes[(cd + '/' + tokens[1])]['size'] = int(tokens[0])

    # check that tree structure is intact
    if not (nx.is_arborescence(G)):
        raise Exception('Not a tree!')

# node size
def calc_node_size(node):
    n = G.nodes[node]
    if 'size' not in n:
        succ_tot_size = 0
        for succ in list(G.successors(node)):
            succ_tot_size += calc_node_size(succ)
        n['size'] = succ_tot_size
    return n['size']

# part 1
sum_size = 0
# part 2
min_dir_size_to_delete = 70000000

# final sweep to compute directory size
for node, node_data in G.nodes.items():
    if node_data['type'] == 'directory':
        node_size = calc_node_size(node)
        #part 1
        if node_size <= 100000:
            sum_size += node_size
        #part 2
        min_space_to_free = 30000000 - (70000000 - G.nodes['/']['size'])
        if node_size >= min_space_to_free and node_size < min_dir_size_to_delete:
            min_dir_size_to_delete = node_size

print(f'The sum of directories with a size less than 100000 is {str(sum_size)}')
print(f'The directory to be deleted to get enough space has a size of {str(min_dir_size_to_delete)}')

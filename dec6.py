## December 6

# Define a tree class
class Tree:
    """Tree implementation
    Attributes:
        parents: list of the parent of each node. Root has empty entry.
        children: list of the children of each node. Empty entry if no children.
        data: Data of each node.
        depth: In which level the node sits. Root is at 0."""
    
    def __init__(self,root_data):
        self.parents = [[]]
        self.children = [[]]
        self.data = [root_data]
        self.depth = [0]
        
    def add_node_by_index(self,parent,node_data):
        self.parents.append(parent)
        self.children[parent].append(len(self.parents)-1)
        self.children.append([])
        self.data.append(node_data)
        self.depth.append(self.depth[parent]+1)
        
    def add_node_by_name(self,parent_name,node_data):
        """Assumes that the name is stored in .data and is unique!"""
        self.parents.append(self.data.index(parent_name))
        self.children[self.parents[-1]].append(len(self.parents)-1)
        self.children.append([])
        self.data.append(node_data)
        self.depth.append(self.depth[self.parents[-1]]+1)


# Define collect all parents function
def collect_parents(tree,node_name):
    current_parent = tree.parents[tree.data.index(node_name)]
    all_parents = set([])
    while current_parent!=0:
        all_parents.add(tree.data[current_parent])
        current_parent = tree.parents[current_parent]
    
    else:
        all_parents.add('COM')
        return(all_parents)
    

# Read input
with open('dec6_input.txt','r') as fin:
# with open('example.txt','r') as fin:
    data=fin.read().splitlines()
    parents,children=[x.split(')')[0] for x in data],[x.split(')')[1] for x in data]



## Build tree
# Initialise instance with root name
tree_inst=Tree('COM')
# Initialise with 'COM' as current node and placeholder as next node
current_node='COM'
next_nodes=[0] 
# Build the tree top down
while len(parents)>0:
    # Check if there are nodes that have the current node as parent
    while current_node in parents:
        # Find index of next occurence of the node as a parent
        ind=parents.index(current_node)
        # Add node
        tree_inst.add_node_by_name(current_node, children[ind])
        # Add the child as a next node and erase the current entry from both lists
        next_nodes.append(children.pop(ind))
        del parents[ind]
    
    else:
        current_node=next_nodes.pop(0)

# Part 1: count direct and indirect orbits        
print(sum(tree_inst.depth))

# Part 2: find shortest path
# Collect parents
my_parents = collect_parents(tree_inst,'YOU')
santas_parents = collect_parents(tree_inst, 'SAN')

common_parents = list(santas_parents.intersection(my_parents))
depths = [tree_inst.depth[tree_inst.data.index(x)] for x in common_parents]

print(my_parents)
print(santas_parents)
print(common_parents)
print(depths)


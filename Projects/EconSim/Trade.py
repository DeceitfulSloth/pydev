# We will begin by creating a graph

class Node:
    id = 0
    name = ''
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Edge:
    id1 = 0
    id2 = 0
    
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

class Graph:
    nodes = []
    edges = []

    def __init__(self):
        print('Graph instantiated')
        self.id_incrementor = 0
    
    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_name_by_id(self, id):
        for x in self.nodes:
            if x.id == id:
                return x.name
        raise Exception('The id:' + id + ' was not found in the graph')

    def get_edges_with_node_names(self):
        dat = []
        for x in self.edges:
            dat.append((self.get_name_by_id(x.id1),self.get_name_by_id(x.id2)))
        return dat

    def get_edges_with_id(self):
        dat = []
        for x in self.edges:
            dat.append((x.id1,x.id2))
        return dat

def makeRandomGraph(num_nodes, num_edges):
    x = Graph()
    for i in range(num_nodes):
        x.add_node(i,str(i))

    for i in range(num_edges):
        

# Create Graph
x = Graph()

# Add some nodes
x.add_node(Node(0,'Alice'))
x.add_node(Node(1,'Bob'))
x.add_node(Node(2,'Charlie'))

# Add some edges
x.add_edge(Edge(0,1))
x.add_edge(Edge(0,2))
x.add_edge(Edge(1,2))


print('x has the following nodes:')
for i in x.get_nodes():
    print(i.name)
print('')

print('x has the following connections:')
for i in x.get_edges():
    print(str(i.id1) + ' - ' + str(i.id2))
print('')

print('This corresponds to connections between these pairs of people:')
print(x.get_edges_with_node_names())




print('')
print('done')
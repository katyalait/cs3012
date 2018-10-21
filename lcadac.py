# -- Lowest Common Ancestor in Directed Acyclic Graph Implementation
# -- Ekaerina Lait
# -- laite@tcd.ie

class Graph:
    # Graph stores nodes in an adjacency list of dictionaries
    # with node key as the key and set of parent nodes as the value.
    # Note: As it is a directed graph node pairs are not
    # symmetrical i.e. a child node points to its parent
    # node but not vice versa.
    #self.graph = {}
    def __init__(self):
        # Initialise graph with empty set
        self.graph = {"A": set()}

    def __init__(self, graph):
        self.graph = graph

    def add_child(self, key, parent):
        self.graph[key]= set(parent)
        return parent

    def add_parent(self, key, parent_to_add):
        #extracts adjacency set for a key and adds parent to set
        self.graph[key].add(parent_to_add)
        return parent_to_add

    def findLCADAG(self, root, first, second):
        # Takes in first node key and second node key
        # Returns lowest common Ancestor key
        yield

    def bfs(self, root, start):
        visited = set() #initialise empty set of visited keys
        #key, value pair of vertex to path
        queue = [(start, [start])]
        paths = [] #create a tuple which will return paths
        while queue:
            (node, path) = queue.pop(0) #enqeue node
            for vertex in self.graph[node]:
                #iterates through set of parents
                if vertex == root:
                    paths.append(path + [vertex])
                else:
                    queue.append((vertex, path + [vertex]))
        return paths

    def print_paths(self, paths):
        return_str = ""
        for path in paths:
            for vertex in path:
                return_str += ""+str(vertex)+" --> "
            return_str+= "END\n"
        return return_str

# -- Lowest Common Ancestor in Directed Acyclic Graph Implementation
# -- Ekaerina Lait
# -- laite@tcd.ie

class Graph:
    # Graph stores nodes in an adjacency list of dictionaries
    # with node key as the key and adjacent nodes as a set.
    # Note: As it is a directed graph node pairs are not
    # symmetrical i.e. a child node points to its parent
    # node but not vice versa.

    def __init__(self):
        # Initialise graph with empty set
        self.graph = {"A": set()}

    def __init__(self, graph):
        self.graph = graph

    def add_child(self, key, parent):
        self.graph.append(key: set(parent))
        return parent

    def add_parent(self, key, parent_to_add):
        #extracts adjacency set for a key and adds parent to set
        self.graph[key].add(parent_to_add)
        return parent_to_add

    

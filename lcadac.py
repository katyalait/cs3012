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

    def add_graph(self, graph):
        self.graph = graph

    def add_child(self, key, parent):
        self.graph[key]= set(parent)
        return parent

    def add_parent(self, key, parent_to_add):
        #extracts adjacency set for a key and adds parent to set
        self.graph[key].add(parent_to_add)
        return parent_to_add

    def findLCADAG(self, root, nodes):
        # Takes in list of nodes
        # Returns lowest common ancestor key(s)
        trace = []
        while nodes:
            node = nodes.pop(0)
            paths = []
            if self.bfs(root, node, paths):
                trace.append(paths)
            else:
                return [-1]
        print(self.print_paths(trace))
        paths_a = trace.pop(0)
        paths_b = trace.pop(0)
        ancestor = ""
        max_height = 0
        lowest_ancestor = ""
        i=0
        for path1 in paths_a:
            for path2 in paths_b:
                i = 1
                while(i <= len(path1) and i <= len(path2)):
                    print("Comparing " + path1[-i] + " and " + path2[-i] + "...")
                    if(path2[-i]!=path1[-i]):
                        print("No match! Breaking at " + path1[-i])
                        break
                    i = 1 + i
                if max_height < i:
                    max_height = i
                    print("New LCA: " + path1[-i+1])
                    lowest_ancestor = path1[-i+1]
        print("The lowest ancestor is " + str(lowest_ancestor))
        return lowest_ancestor


    def bfs(self, root, start, paths):
        if root not in self.graph:
            print("Root not in graph")
            return False
        if start not in self.graph:
            print("Node not in graph")
            return False
        #key, value pair of vertex to path
        queue = [(start, [start])]
        while queue:
            (node, path) = queue.pop(0) #enqeue node
            for vertex in self.graph[node]:
                #iterates through set of parents
                if vertex == root:
                    paths.append(path + [vertex])
                else:
                    queue.append((vertex, path + [vertex]))
        return True

    def print_paths(self, paths):
        return_str = ""
        for path in paths:
            for vertex in path:
                return_str += ""+str(vertex)+" --> "
            return_str+= "END\n"
        return return_str

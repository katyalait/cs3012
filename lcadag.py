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
        for key in graph:
            if not key.isalpha():
                print("Key " + key +" not alphabetical")
                return False
            val = graph[key]
            try:
                #ensure is valud set by performing union with an empty set
                tst = val.union(set())
            except:
                print("Set not valid for key: " + key)
                return False
        self.graph = graph
        return True

    def add_child(self, key, parent):
        if not key.isalpha():
            return False
        try:
            tst = parent.union(set())
        except:
            print("Parent set is not valid")
            return False
        for par in parent:
            try:
                tst = self.graph[par]
            except:
                print("Parent is not a valid key in graph")
                return False
        self.graph[key]= set(parent)
        return True

    def findLCADAG(self, root, nodes):
        # Takes in list of nodes
        # Returns lowest common ancestor key(s)
        trace = []
        for node in nodes:
            paths = []
            if self.bfs(root, node, paths):
                trace.append(paths)
            else:
                return -1
        print(self.print_paths(trace))
        lowest_ancestor = ""
        max_height,i = 0, 0
        for path1 in trace[0]:
            for path2 in trace[1]:
                i = 1
                while(i <= len(path1) and i <= len(path2)):
                    if(path2[-i]!=path1[-i]):
                        break
                    i = 1 + i
                if i>max_height: #if max_height reached
                    max_height=i
                    print("New LCA " + str(path1[-i+1]))
                    lowest_ancestor = path1[-i+1]
                elif i==max_height and lowest_ancestor!=path1[-i+1]:
                    tmp = lowest_ancestor
                    lowest_ancestor = []
                    lowest_ancestor.append(tmp)
                    lowest_ancestor.append(path1[-i+1])
        #check if they share parents
        print("Final LCA: " + str(path1[-i+1]))
        return lowest_ancestor
    def bfs(self, root, start, paths):
        if root not in self.graph:
            return False
        if start not in self.graph:
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

#Script for testing the code in the commandline
import lcadac

my_graph = {"A": set(), #                 A
        "B": set(["A"]),#               /  \
        "C": set(["A"]),#             B     C
        "D": set(["C"]), #             \  /  \
        "E": set(["B", "C"]),#          E     D
        "F": set(["E"]),#             /  \
        "G": set(["E"])}#           G     F
graph = lcadac.Graph()
graph.add_graph(my_graph)
paths = []
graph.bfs("A", "E", paths)
print(graph.print_paths(paths))
#print(graph.findLCADAG("A", ["F", "E"]))
#graph.print_paths()

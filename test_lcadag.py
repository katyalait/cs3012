import pytest
import lcadag

def test_init():
    desired_set = {"A": set()}
    tst_graph = lcadag.Graph()
    assert desired_set == tst_graph.graph

def test_add_graph():
    #1. testing best case
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": set(["B", "C"]),#          E     D
            "F": set(["E"])}#                \
                          #                   F
    tst_graph = lcadag.Graph()
    assert tst_graph.add_graph("A", my_graph)==True
    assert tst_graph.graph == my_graph

    #2. test invalid Key
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "1": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": set(["B", "C"]),#          E     D
            "F": set(["E"])}#                \
                          #                   F
    assert tst_graph.add_graph("A", my_graph)==False

    #3. test invalid value
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": "E and D",#                E     D
            "F": set(["E"])}#                \
                          #                   F
    assert tst_graph.add_graph("A", my_graph) == False

    #4. test invalid root
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": "E and D",#                E     D
            "F": set(["E"])}#                \
                          #                   F
    assert tst_graph.add_graph("1", my_graph) == False
def test_add_child():
    graph = lcadag.Graph()
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": set(["B", "C"]),#          E     D
            "F": set(["E"])}#                \
                          #                   F
    graph.add_graph("A", my_graph)

    #1. test best case
    child = {"G": set(["E", "B"])}
    assert graph.add_child("G", set(["E", "B"]))==True

    #2. test incorrect key
    assert graph.add_child("!", set(["E", "B"]))==False

    #3. test incorrect value
    assert graph.add_child("G", set(["E", "M"]))==False
    assert graph.add_child("G", set(["E", "1"]))==False
    assert graph.add_child("G", "E and B")==False

def test_LCADAG():
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #          /  \  /  \
            "E": set(["B", "C"]),#     G    E     D
            "F": set(["E", "D"]),#        /  \  /  \
            "G": set(["B"]),#           H     F     H
            "H": set(["E", "D"])}
    graph = lcadag.Graph()
    graph.add_graph("A", my_graph)
    #1. test average case
    lca = graph.findLCADAG(["E", "D"])
    assert lca[0] == "C"
    #2. test case where one node is parent of the other
    lca = graph.findLCADAG(["E", "F"])
    assert lca[0] == "E"
    #3. test when nodes have only A in common
    lca = graph.findLCADAG(["D", "G"])
    assert lca[0] == "A"
    #4. test when nodes have many parent nodes
    lca = graph.findLCADAG(["H", "F"])
    assert lca == ["E", "D"] or ["D", "E"]
def test_error_LCADAG():
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #          /  \  /  \
            "E": set(["B", "C"]),#     G    E     D
            "F": set(["E", "D"]),#        /  \  /  \
            "G": set(["B"]),#           H     F     H
            "H": set(["E", "D"])}
    graph = lcadag.Graph()
    graph.add_graph("A", my_graph)

    #1. test for finding nodes not in dict
    lca = graph.findLCADAG(["D", "K"])
    assert lca ==-1
def bfs_test():
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": set(["B", "C"]),#          E     D
            "F": set(["E"])}#                \
                          #                   F
    graph = lcadag.Graph()
    graph.add_graph("A", my_graph)
    paths = []
    #1. test for average case
    graph.bfs("D", paths)
    assert paths == ["D", "C", "A"]
    #2. test for multiple paths case
    paths = []
    graph.bfs("E", paths)
    assert paths == ["E", "C", "A"] or ["E", "B", "A"]
    #3. error test
    paths = []
    assert graph.bfs("K", paths)==False
def test_print():
    my_graph = {"A": set(), #                 A
            "B": set(["A"]),#               /  \
            "C": set(["A"]),#             B     C
            "D": set(["C"]), #             \  /  \
            "E": set(["B", "C"]),#          E     D
            "F": set(["E"])}#                \
                          #                   F
    graph = lcadag.Graph()
    graph.add_graph("A", my_graph)
    paths = []
    graph.bfs("D", paths)
    assert graph.print_paths(paths)== "D --> C --> A --> END\n"
    paths = []
    graph.bfs("E", paths)
    #print(graph.print_paths(paths))
    assert graph.print_paths(paths) == "E --> C --> A --> END\nE --> B --> A --> END\n" or "E --> B --> A --> END\nE --> C --> A --> END\n"

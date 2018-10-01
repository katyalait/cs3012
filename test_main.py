import pytest
import lca

# class test_LCA(unittest.TestCase):

#test result for no input
def test_answer1():
    assert lca.findLCA(None, None, None) == -1

#test when both nodes are the root node
def test_answer2():
    root = lca.Node(1)
    assert lca.findLCA(root,1,1) == 1

#test add_node function
def test_add_node1():
    root = lca.Node(4)
    root.add_node(2)
    root.add_node(5)
    assert lca.findLCA(root,2,5) == 4

def test_add_node2():
    root = lca.Node(4)
    root.add_node(2)
    root.add_node(5)
    assert lca.findLCA(root, 2, 3) == -1

def test_add_node3():
    root = lca.Node(4)                   #4
    root.add_node(2)                 #2      5
    root.add_node(5)             #1     3       8
    root.add_node(1)            #              7
    root.add_node(3)
    root.add_node(8)
    root.add_node(7)
    root.add_node(10)
    assert lca.findLCA(root,7, 10) == 8

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

#test when value is not in the tree
def test_add_node1():
    root = lca.Node(4)
    root.add_node(2)
    root.add_node(5)
    assert lca.findLCA(root,2,5) == 4

import pytest
import main

# class test_LCA(unittest.TestCase):

#test result for no input
def test_answer1():
    assert main.findLCA(None, None, None) == None

#test when both nodes are the root node
def test_answer2():
    root = main.Node(1)
    assert main.findLCA(root,1,1) == 1

#test when value is not in the tree
def test_add_node1():
    root = main.Node(4)
    root.add_node(2)
    root.add_node(5)
    assert main.findLCA(root,2,5) == 4


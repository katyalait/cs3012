import random

class Node:
#defining the node class
    def __init__(self, key): #self selection and the key of the node
        self.key = key
        self.left = None
        self.right = None
    #recursive function to create nodes
    def add_node(self, key):
        if self.left==None:
            self.left = Node(key)
        elif self.right==None:
            self.right = Node(key)
        else:
            if key < self.key:
                self.left.add_node(key)
            else:
                self.right.add_node(key)


def create_tree(root, min, max):
    new_root = Node(root)
    i = min
    j = max
    while(i <= j):
        new_root.add_node(i)
        i = i + 1
    return new_root


#recursive function which takes in a root,
#a path list and k destination key
def findPath(root, path, k):
    if root is None:
        return False
    path.append(root.key)
    if root.key == k:
        return True
    if ((root.left != None and findPath(root.left, path, k)) or
        (root.right != None and findPath(root.right, path, k))):
        return True
    path.pop()
    return False

def findLCA(root, n1, n2):
    #define paths globally so their values can be stored
    path1 = []
    path2 = []

    if (not findPath(root, path1,n1) or not findPath(root, path2, n2)):
        return -1
    #test path likeness here
    i = 0
    while(i < len(path1) and i < len(path2)):
        if(path2[i]!=path1[i]):
            break
        i = 1 +i
    return path1[i-1] #return the last valid ancestor

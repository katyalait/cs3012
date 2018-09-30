class Node:
#defining the node class
    def __init__(self, key): #self selection and the key of the node
        self.key = key
        self.left = None
        self.right = None

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

def findLCAns(root, n1, n2):
    #define paths globally so their values can be stored
    path1 = []
    path2 = []

    if (not findPath(root, path1,n1) or not findPath(root, path2, n2)):
        return -1
    #test path likeness here
    i = 0
    while(i < len(path1) && i < len(path2)):
        if(path2[i]!=path1[i]):
            break
        i++
    return path1[i-1] #return the last valid ancestor

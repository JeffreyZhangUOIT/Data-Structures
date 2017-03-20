import math
class Tree(object):
    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data

    def hasLeft(self):
        return self.right

    def hasRight(self):
            return self.left

    def addChild(n):
        if (Tree.hasLeft()):
            if (Tree.hasRight()):
                return None
            Tree.right = n
        else:
            Tree.left = n



    def data(self):
        return self.data


preorder = input('Please enter your Preorder Sequence: ')

leftChild = None
rightChild = None
a = [i for i in preorder]
depth = math.ceil(math.sqrt(len(a)))
middle = math.pow(2, depth)/2
node = 0

def buildTree(a, node, middle, depth ):
    if depth == 0:
        tNode = Tree(a[node])
        return
    tNode = Tree(a[node], a[node+1], a[middle+1])

    B, C = a[:middle], a[middle+1:]
    depth = depth - 1
    middle = math.floor(math.pow(2, depth)/2 )

    buildTree(B, B[node+1], B[middle], depth)
    buildTree(C, C[node+1], C[middle], depth)

buildTree(a, node, middle, depth)


def postOrder(tree):
    if tree == None: return
    postOrder(tree.hasLeft())
    postOrder(tree.hasRight())
    print tree.data
    return

#postOrder(a[1])

import math
class Tree(object):
    def __init__(self, data):
        self.data = data

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


def buildTreePreorder(a):
    depth = int(math.ceil(math.log(len(a), 2)))
    middle = int(math.floor(math.pow(2, depth) / 2))
    if depth <= 1:
        tNode = Tree(a[0], None, None)
        return
    else:

        tNode = Tree(a[0], a[1], a[middle+1])
        a.pop(0)
        b, c = a[:middle], a[middle+1:]
        depth = depth - 1
        buildTreePreorder(b)
        buildTreePreorder(c)

buildTreePreorder(a)


def postOrder(tree):
    if tree == None: return
    postOrder(tree.hasLeft())
    postOrder(tree.hasRight())
    print tree.data
    return

#postOrder(a[1])

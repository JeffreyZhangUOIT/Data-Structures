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

    def addChild(self, val):
        if (self.left != None):
            if (self.right != None):
                print 'could not add child.'
                return
            else:
                self.right = Tree(val, None, None)
        else:
            self.left = Tree(val, None, None)
        return



    def data(self):
        return self.data


preorder = input('Please enter your Preorder Sequence: ')

leftChild = None
rightChild = None
a = [i for i in preorder]
tNode = Tree(1, None, None)
a.pop(0)

def buildTreePreorder(a, tNode):
    if tNode == None:
        return
    if len(a) == 0:
        return
    else:
        depth = int(math.ceil(math.log(len(a), 2)))
        middle = int(math.floor(math.pow(2, depth) / 2))
        if depth == 0:
            Node = Tree(a[0], None, None)
            return
        else:
            tNode.addChild(a[0])
            if depth == 1:
                middle = 2
            if depth == 2:
                middle = 3
            tNode.addChild(a[middle-1])
            print 'added left child', a[0], 'and right child', a[middle-1], 'to ', tNode.data
            print a
            print
            a.pop(0)
            b, c = a[:middle-2], a[middle-1:]
            buildTreePreorder(b, tNode.left)
            buildTreePreorder(c, tNode.right)

buildTreePreorder(a, tNode)


def preOrder(tree):
    if tree == None: return
    print tree.data
    preOrder(tree.left)
    preOrder(tree.right)
    return

preOrder(tNode)
# 1,2,3,4,5,6,7,8,9,10,11,12

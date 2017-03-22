import math

def postOrder(tree):
    if tree == None: return
    postOrder(tree.left)
    postOrder(tree.right)
    print tree.data,
    return

def preOrder(tree):
    if tree == None: return
    print tree.data,
    preOrder(tree.left)
    preOrder(tree.right)
    return

def inOrder(tree):
    if tree == None: return
    inOrder(tree.left)
    print tree.data,
    inOrder(tree.right)

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
                print 'could not add child. left and right children are:', self.left.data, self.right.data
                return
            else:
                self.right = Tree(val, None, None)
        else:
            self.left = Tree(val, None, None)
        return



    def data(self):
        return self.data

def buildTreePreorder(array, tNode):
    if tNode == None:
        return
    if len(array) == 0:
        return
    else:
        depth = int(math.ceil(math.log(len(array), 2)))
        middle = int(math.floor(math.pow(2, depth) / 2))
        if depth == 0:
            tNode.addChild(array[0])
            return
        else:
            tNode.addChild(array[0])
            if depth == 1:
                middle = 2
            if depth == 2:
                middle = 3
            tNode.addChild(array[middle-1])
            array.pop(0)
            b, c = array[:middle-2], array[middle-1:]
            buildTreePreorder(b, tNode.left)
            buildTreePreorder(c, tNode.right)

def buildTreeInorder(array, tNode):
    if len(array) == 0:
        return
    else:
        depth = int(math.ceil(math.log(len(array), 2)))
        middle = int(math.floor(math.pow(2, depth) / 2))
        if depth == 0:
            return array[0]
        else:
            b, c = array[:middle - 1], array[middle:]
            lowerb = len(b) / 2
            lowerc = len(c)/2
            if len(b) == 0:
                return
            if len(c) == 0:
                return
            tNode.addChild(b[lowerb])
            tNode.addChild(c[lowerc])
            buildTreeInorder(b, tNode.left)
            buildTreeInorder(c, tNode.right)
            return array[middle-1]

sequence = input('Please enter your Sequence: ')

leftChild = None
rightChild = None
preorder = [i for i in sequence]
preTree = Tree(1, None, None)
preorder.pop(0)
buildTreePreorder(preorder, preTree)

inorder =[i for i in sequence]
inTree = Tree(8, None, None)
buildTreeInorder(inorder, inTree)

print 'for preorder traversal.'
print 'post-order: '
postOrder(preTree)

print
print 'in-order: '
inOrder(preTree)


print
print
print 'for inorder traversal'
print 'pre-order: '
preOrder(inTree)

print
print 'post-order: '
postOrder(inTree)



# 1,2,3,4,5,6,7,8,9,10,11,12

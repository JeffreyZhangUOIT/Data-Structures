"""
    This program creates a binary tree out of the given inputs in the form: n1,n2,n3,n4,n5
    assuming it either given in the form of preorder, inorder or postorder traversal.
    It will then output the traversals using the other two methods.
"""
import math
"""
    These three recursive methods are for traversing a binary tree in
    preorder, inorder, and postorder. The only difference between each method
    is the when the current node's data is printed. 
"""
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

def postOrder(tree):
    if tree == None: return
    postOrder(tree.left)
    postOrder(tree.right)
    print tree.data,
    return

"""
    This is the abstract data structure for a binary tree. In this implementation,
    a tree is defined as a node carrying data and two references to two subtrees.
    The tree inherits from the default object class. Unneccessary functions that
    are common to binary trees such as editing and removing a node have been
    omitted.

    __init__(self, data, left, right) is the constructor for each tree. A null node would be initalised as Tree(None, None, None)
    self: The instance of tree which called this constructor.
    data: The data of the current node
    left: The left subtree
    right: The right subtree

    addChild(self, val) is a function that adds a subtree who's data is given as val. 
    This will always populate a left child before a right child.
    self: The instance of tree which called this method
    val: The data to be carried by the subtree.

"""
class Tree(object):

    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data

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
"""
    buildTreePreorder(list, tNode) is a method which creates a binary tree given an list of of data values and a Tree object.
    We accomplish this by assigning the current node's children as the first and middle element of the list. This is always the case
    when given a preorder traversal. We then recursively call this method with an list b and list c. This method requires initialising
    the list tNode with the first piece of data already set.

    list: An list carrying the remainder of the unassigned data
    tNode: The current node in a binary tree.
    depth: This is the current height of the tree given the length of the list, cased into an integer.
    middle: This is the index of the middle of the list + 1 calculated using the height of the list; casted into an integer.
    b: The first 2^n elements which makes up the first 'half' of the list. n is the depth.
    c: The remainder of the list

"""
def buildTreePreorder(list, tNode):
    if len(list) == 0:
        return
    else:
        depth = int(math.ceil(math.log(len(list), 2)))
        middle = int(math.floor(math.pow(2, depth) / 2))
        if depth == 0:
            tNode.addChild(list[0])
            return
        else:
            tNode.addChild(list[0])
            if depth == 1:
                middle = 2
            if depth == 2:
                middle = 3
            tNode.addChild(list[middle-1])
            list.pop(0)
            b, c = list[:middle-2], list[middle-1:]
            buildTreePreorder(b, tNode.left)
            buildTreePreorder(c, tNode.right)
"""
    buildTreeInorder(list, tNode) is a method which creates a binary tree given an list of of data values and a Tree object.
    We accomplish this by first assiging the current node's data value as the center of the list. It will then split the list
    into two subsets, b and c, such that b is the first 2^n elements and c is the remaining elements. n is the depth of the
    current tree, calculated from the number of elements in the list. The node's children
    are then assigned as the center of each new list b and c. This is a property of in-order traversal.

    list: The unassigned elements in a post-order traversal of a binary tree.
    tNode: The current node in a binary tree.
    depth: This is the current height of the tree given the length of the list, cased into an integer.
    middle: This is the index of the middle of the list + 1 calculated using the height of the list; casted into an integer.
    b: The first 2^n elements which makes up the first 'half' of the list. n is the depth.
    c: The remainder of the list
"""
def buildTreeInorder(list, tNode):
    if len(list) == 0:
        return
    else:
        depth = int(math.ceil(math.log(len(list), 2)))
        middle = int(math.floor(math.pow(2, depth) / 2))
        if depth == 0:
            return list[0]
        else:
            b, c = list[:middle - 1], list[middle:]
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
            return list[middle-1]


"""
    buildTreePostorder(list, tNode) is a method which creates a binary tree given an list of of data values and a Tree object.
    We accomplish this by first assiging the current node's data value the last element of an list. Then we remove the last element
    from the list. It will then split the list into two subsets, b and c, such that b is the first 2^n elements and c is the
    remaining elements. n is the depth of the current tree, calculated from the number of elements in the list. The node's children
    are assigned as the last element of each new list b and c. This is a property of post-order traversal.

    list: The unassigned elements in a post-order traversal of a binary tree.
    tNode: The current node in a binary tree.
    depth: This is the current height of the tree given the length of the list, cased into an integer.
    middle: This is the index of the middle of the list + 1 calculated using the height of the list; casted into an integer.
    b: The first 2^n elements which makes up the first 'half' of the list. n is the depth.
    c: The remainder of the list
"""
def buildTreePostorder(list, tNode):
    if len(list) == 0:
        return
    else:
        depth = int(math.ceil(math.log(len(list), 2)))
        middle = int(math.floor(math.pow(2, depth) / 2))
        if depth == 0:
            tNode = Tree(list[0], None, None)
            return

        tNode.data = list.pop()
        b, c = list[:middle-1], list[middle-1:]
        if len(b) == 0:
            tNode.left = None
        else:
            tNode.addChild(b[len(b) - 1])
            buildTreePostorder(b, tNode.left)
        if len(c) == 0:
            tNode.right = None
        else:
            tNode.addChild(c[len(c) - 1])
            buildTreePostorder(c, tNode.right)

# Ask the user for a list of data points in a binary tree.
sequence = input('Please enter your Sequence: ')

# Creates an list from the given sequence, and builds the tree as if it was given preorder traversal
preorder = [i for i in sequence]
preTree = Tree(preorder[0], None, None)
preorder.pop(0)
buildTreePreorder(preorder, preTree)

# Outputs the other forms of traversal from the preorder tree.
print 'for preorder traversal'
print 'post-order: '
postOrder(preTree)

print
print 'in-order: '
inOrder(preTree)

# Creates an list from the given sequence and builds the tree as if it was given inorder traversal
print
inorder =[i for i in sequence]
inTree = Tree(8, None, None)
buildTreeInorder(inorder, inTree)

# Outputs the other forms of traversal from the in-order tree
print
print 'for inorder traversal'
print 'pre-order: '
preOrder(inTree)

print
print 'post-order: '
postOrder(inTree)

# Creates an list from the given sequence and builds the tree as if it was given post-order traversal
print
postorder = [i for i in sequence]
postTree = Tree(0, None, None)
buildTreePostorder(postorder, postTree)

# Prints the other forms of traversal from the post-order tree
print
print 'for postorder:'
print 'pre-order: '
preOrder(postTree)
print
print 'in-order: '
inOrder(postTree)

# Example Sequence:
# 1,2,3,4,5,6,7,8,9,10,11,12
"""
    If you want to check if the tree is built correctly,
    run the preorder traversal on the preorder tree.
    The other variations postorder and inorder also work.
"""

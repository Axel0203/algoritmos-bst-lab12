class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
def insertNode(root, node):
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)
                 
def findMin(root):
    currentNode = root
    if currentNode.left == None:
        return currentNode
    else:
        return findMin(currentNode.left)
 
def findMax(root):
    currentNode = root
    if currentNode.right == None:
        return currentNode
    else:
        return findMax(currentNode.right)

def buildManualBST():
    root = BSTNode(5)
    insertNode(root, BSTNode(7))
    insertNode(root, BSTNode(3))
    insertNode(root, BSTNode(9))
    insertNode(root, BSTNode(1))
    insertNode(root, BSTNode(12))
    insertNode(root, BSTNode(0))
    return root

def buildBSTFromArray(list):
    root = None
 
    for item in list:
        if list.index(item) == 0:
            root = BSTNode(item)
        else:
            insertNode(root, BSTNode(item))
    return root

def find(root, data):
    currentNode = root
 
    if currentNode == None:
        return None
    else:
        if data == currentNode.data:
            return currentNode.data
        if data < currentNode.data:
            return find(currentNode.left,data)
        else:
            return find(currentNode.right,data)
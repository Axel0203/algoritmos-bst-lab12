"""

"""


# Function to  print level order traversal of tree
def printLevelOrder(root, buffer = None):
    h = height(root)
    #print(h)
    for i in range(1, h+1):
        printCurrentLevel(root, i, buffer=buffer)
  
# Print nodes at a current level
def printCurrentLevel(root , level , data="" ,side ="D",  pattern = "\n", buffer = None ):
    if root is None:
        return
    if level == 1:
        if buffer is not None : 
            buffer.append(data+side+str(root.data))
        print(data+side+str(root.data),end=pattern)
    elif level > 1 :  
        printCurrentLevel(root.left ,level-1,f"D{root.data}","L",  " ", buffer = buffer)
        printCurrentLevel(root.right,level-1,f"D{root.data}","R", "\n", buffer = buffer )
 
""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

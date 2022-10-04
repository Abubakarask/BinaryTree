class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""Print Tree"""
def printTree(root):
    if root is None:
        return

    print(root.data, end=":")

    if root.left:
        print("L", root.left.data, end=",")
    if root.right:
        print("R", root.right.data, end=" ")
    print()
    printTree(root.left)
    printTree(root.right)
  
"""Create Binary Tree using Input"""
"""1.Complex while taking input"""
def TreeInput():
    rootData = int(input(' '))

    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)

    leftTree = TreeInput()
    rightTree = TreeInput()
    root.left = leftTree
    root.right = rightTree

    return root

root = TreeInput()
printTree(root)


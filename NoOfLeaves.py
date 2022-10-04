def numLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    leftCount = numLeaf(root.left)
    rightCount = numLeaf(root.right)

    return leftCount + rightCount

print(numLeaf(root))

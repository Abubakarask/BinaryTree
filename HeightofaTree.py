def height(root):
    if root is None:
        return 0

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return 1+max(leftHeight, rightHeight)

print(height(root))

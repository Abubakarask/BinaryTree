def maximumValue(root):
    if root is None:
        return -1

    leftmax = maximumValue(root.left)
    rightmax = maximumValue(root.right)

    return max(leftmax,rightmax, root.data)

print(maximumValue(root))

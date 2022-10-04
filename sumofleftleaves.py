def leftLeavesSum(root):
    res = 0

    if root is not None:
        if isLeaf(root.left):
            res += root.left.data
        else:
            res += leftLeavesSum(root.left)

        res += leftLeavesSum(root.right)
    return res

print(leftLeavesSum(root))

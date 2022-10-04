"""Determine whether Tree is Balanced or Not"""

"""Solution 1 TC is more"""
# def Height(root):
#     if root is None:
#         return 0
#
#     leftHeight = Height(root.left)
#     rightHeight = Height(root.right)
#
#     return 1 + max(leftHeight, rightHeight)
#
# def Balanced(root):
#     if root is None:
#         return True
#
#     leftHeight = Height(root.left)
#     rightHeight = Height(root.right)
#
#     if abs(leftHeight - rightHeight) > 1:
#         return False
#
#     isLeftBalanced = Balanced(root.left)
#     isRightBalanced = Balanced(root.right)
#
#     if isLeftBalanced and isRightBalanced:
#         return True
#     else:
#         return False
#
# print(Balanced(root))

"""Optimized Solution"""
def isBalanced2(root):
    if root is None:
        return 0, True

    lefthei, isleftBalanced = isBalanced2(root.left)
    righthei, isrightBalanced = isBalanced2(root.right)

    h = 1 + max(lefthei, righthei)

    if abs(lefthei - righthei) > 1:
        return h, False

    if isleftBalanced and isrightBalanced:
        return h, True
    else:
        return h, False

print(isBalanced2(root))

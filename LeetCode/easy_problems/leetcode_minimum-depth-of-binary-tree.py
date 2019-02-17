# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0

        if root.left is None and root.right is None:  # leaf node
            return 1

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        min_depth = min(left, right)

        return 1 + min_depth


# test cases
# solution = Solution()
#
# [3, 9, 20, None, None, 15, 7]
# [1, 2]
#
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
#
# solution.minDepth(root)
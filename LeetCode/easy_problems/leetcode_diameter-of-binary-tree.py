# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tree_max_diameter = 0  # if the tree does not have any subtrees on either side

        self.no_of_nodes(root)

        return self.tree_max_diameter

    def no_of_nodes(self, node):

        # this is the base case, where the node is null
        if node is None:
            return 0

        # traverse a node down to its leaves
        else:
            left_subtree_height = self.no_of_nodes(node.left)
            right_subtree_height = self.no_of_nodes(node.right)

            # update the diameter as we're traversing the node
            max_diameter = max(self.tree_max_diameter, left_subtree_height + right_subtree_height)

            if max_diameter > self.tree_max_diameter:
                self.tree_max_diameter = max_diameter

            return max(left_subtree_height, right_subtree_height) + 1


# test cases
# solution = Solution()
#
# # [1, 2, 3, 4, 5]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# solution.diameterOfBinaryTree(root)
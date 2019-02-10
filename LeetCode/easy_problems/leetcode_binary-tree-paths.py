# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        if root is None:  # if the root is None, don't proceed
            print(f'root is None {root}')
            return []

        if root.left is None and root.right is None:  # this is the leaf node
            print(f'root left and right are none, leaf is {[str(root.val)]}')
            return [str(root.val)]

        print(f'root is {root.val}')

        print('calling left binary path')
        left = self.binaryTreePaths(root.left)
        print(f'root left is {left}')

        print('calling right binary path')
        right = self.binaryTreePaths(root.right)
        print(f'root right is {right}')

        subtrees = left + right
        print(f'subtrees is {subtrees}')

        tree_paths = []

        for leaf in subtrees:
            print(f'leaf is {leaf}')

            print(f'tree paths before append is {tree_paths}')
            tree_paths.append(str(root.val) + '->' + leaf)
            print(f'tree paths after append is {tree_paths}')

        return tree_paths


# test cases
# solution = Solution()
#
# [1, 2, 3, 5]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
#
# solution.binaryTreePaths(root)
# Output ["1->2->5", "1->3"]

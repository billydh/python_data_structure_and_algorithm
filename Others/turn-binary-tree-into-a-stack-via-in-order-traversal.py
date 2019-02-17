class TreeNode:
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right = None


def inorder_traversal(stack, root):
    # left, root, right

    if root is None:
        return None

    inorder_traversal(stack, root.left)

    stack.append(root.val)

    inorder_traversal(stack, root.right)

    return stack


# test cases
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

inorder_traversal([], root)

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0
    leftdepth = maxDepth(root.left)
    right = maxDepth(root.right)
    print("leftdepth : ", leftdepth)
    print("right : ", right)

    return 1 + max(right, leftdepth)


if __name__ == "__main__":

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left= TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left= TreeNode(6)
    tree.right.right = TreeNode(75)
    tree.right.right.right = TreeNode(100)

    maxDepth(tree)
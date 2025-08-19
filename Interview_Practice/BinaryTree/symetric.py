class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def symmetric(tree):
    if not tree:
        return True
    
    def ismirror(left ,right):

        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return ismirror(left.left, right.right) and ismirror(left.right, right.left)
        else:
            return False
        
    return ismirror(tree.left, tree.right)


if __name__ == "__main__":

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.right.right = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.left= TreeNode(4)

    print(symmetric(tree))


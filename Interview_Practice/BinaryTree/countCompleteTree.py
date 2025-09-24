class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right






if __name__ == "__main__":

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left= TreeNode(4)
    p.left.right = TreeNode(5)
    p.left.right.right = TreeNode(23)
    p.right.right = TreeNode(7)
    p.right.right.right = TreeNode(100)
    """
            1
          /.  \ 
        2       3
      /. \.    / 
    4      5   7

    """

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, target):

    if not root:
        return False
    if not root.left and not root.right:
        return target == root.val
    return pathSum(root.left, target - root.val) or pathSum(root.right, target - root.val)

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
      /. \.       \  
    4      5        7
            \.       \\
             23       100
    """
    print(pathSum(p, 111))
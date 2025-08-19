
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sameTree(p ,q):

    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return sameTree(p.left, q.left) and sameTree(p.right, q.right)
    else:
        return False





if __name__ == "__main__":

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left= TreeNode(4)
    p.left.right = TreeNode(5)
    p.right.right = TreeNode(75)
    p.right.right.right = TreeNode(100)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.left.left= TreeNode(4)
    q.left.right = TreeNode(5)
    q.right.right = TreeNode(75)
    q.right.right.right = TreeNode(100)

    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left= TreeNode(4)
    r.left.right = TreeNode(5)
    r.right.left= TreeNode(6)
    r.right.right = TreeNode(75)
    r.right.right.right = TreeNode(78)

    print(sameTree(p,r))
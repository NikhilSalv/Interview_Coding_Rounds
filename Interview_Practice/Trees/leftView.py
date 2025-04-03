from collections import deque

class  Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):

    if not root:
        return None
    
    queue = deque([root])
    count = 1

    while queue :
        node = queue.popleft()
        print(node.value, end = " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_preorder(root):
    if root:
        print(root.value,end = " ")
        dfs_preorder(root.left)
        dfs_preorder(root.right)

def left_view(root, max_level = [-1], level = 0, result = []):
    if not root:
        return
    
    if level > max_level[0]:
        result.append(root.value)
        max_level[0]  = level
    if root:
        left_view(root.left, max_level, level +1, result)
        left_view(root.right, max_level, level +1, result)

    return result
    

if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.left.left.left = Tree(6)
    root.left.left.right = Tree(7)
    root.left.left.left.right = Tree(8)
    root.left.right.left = Tree(9)
    root.right.left = Tree(10)
    root.right.right = Tree(11)
    root.right.right.left = Tree(12)
    root.right.right.right = Tree(13)
    # dfs_preorder(root)
    result = left_view(root)
    print(result)




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.max_level = -1
        self.left_view_list = []

    def preorder(self, node): # (Root -> Left -> Right)
        if node:
            print(node.value , "\n")
            self.preorder(node.left)
            self.preorder(node.right)


    def inorder(self, node): # (Left -> Root -> Right)
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def postorder(self, node): # (Left -> Right -> Root)
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, "\n")

    def left_view_until(self, node, level):

        if not node:
            return
        if level > self.max_level:
            self.max_level = level
            self.left_view_list.append(node.value)
        self.left_view_until(node.left, level +1)
        self.left_view_until(node.right, level +1)
    
    def left_view(self):
        self.max_level = -1
        self.left_view_list = []

        self.left_view_until(self.root, 0)
        return self.left_view_list

            


if __name__ == "__main__":

    tree = Tree(1)
    # print(tree.root.value)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7) 
    tree.root.left.left.right = Node(8)
    tree.root.left.left.left = Node(99)
    # print(tree.root.left.right.value)

    # print ("Preorder")
    # tree.preorder(tree.root) # 1 > 2 > 4 > 5 > 3 > 6 > 7
    # tree.inorder(tree.root) # 4 > 2 > 5 > 1 > 6 > 3 > 7
    # tree.postorder(tree.root) # 4 > 5 > 2 > 6 > 7 > 3 > 1

    print(tree.left_view())
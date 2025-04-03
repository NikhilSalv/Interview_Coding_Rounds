class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)
        # self.max_level = -1
        # self.left_view_list = []
        # self.height = -1

    # def preorder(self, node): # (Root -> Left -> Right)
    #     if node:
    #         print(node.value , "\n")
    #         self.preorder(node.left)
    #         self.preorder(node.right)


    # def inorder(self, node): # (Left -> Root -> Right)
    #     if node:
    #         self.inorder(node.left)
    #         print(node.value)
    #         self.inorder(node.right)

    # def postorder(self, node): # (Left -> Right -> Root)
    #     if node:
    #         self.postorder(node.left)
    #         self.postorder(node.right)
    #         print(node.value, "\n")

    # def left_view_until(self, node, level): # Using preorder
    #     if not node:
    #         return
    #     if level > self.max_level:
    #         self.max_level = level
    #         self.left_view_list.append(node.value)
    #     self.left_view_until(node.left, level +1)
    #     self.left_view_until(node.right, level +1)
    
    # def left_view(self):
    #     self.max_level = -1
    #     self.left_view_list = []

    #     self.left_view_until(self.root, 0)
    #     return self.left_view_list
    
    # def heght_of_tree(self, node, depth):
    #     """
    #     edge case
    #     if tree is null : return 0
    #     """
    #     if not node:
    #         print("node is null")
    #         return 0
        
    #     if node:
    #         print("Depth", depth, " Height", self.height)
    #         if depth > self.height:
    #             print("in")
    #             self.height = depth
    #         self.heght_of_tree(node.left, depth+1)
    #         self.heght_of_tree(node.right, depth + 1)
    #     return self.height
    
    def height_of_tree(self, node):
        """
        Returns the height of the tree.
        Edge case: If tree is empty, return -1 (for edge height) or 0 (for node height).
        """
        if not node:
            return -1  # Edge height, change to 0 if considering node height

        # Recursively calculate height of left and right subtrees
        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)

        # Height of current node = max(left height, right height) + 1
        return max(left_height, right_height) + 1
            

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

    # print(tree.left_view())
    print(tree.height_of_tree(tree.root))
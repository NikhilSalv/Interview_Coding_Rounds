class Node:
    def __init__(self, data, next_node = None,random_node = None):
        self.data = data
        self.next_node = next_node
        self.random_node = random_node

def deep_copy(head):
    map_node = {}
    temp = head
    
    while temp:
        newNode = Node(temp.data)
        map_node[temp] = newNode
        temp = temp.next_node

    temp = head
    print(map_node)

    while temp:
        copyNode = map_node[temp]
        copyNode.next_node = map_node[temp.next_node]
        copyNode.random_node = map_node[temp.random_node]

        temp = temp.next_node

    return map_node[head]


if __name__ == "__main__":
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)

    

    
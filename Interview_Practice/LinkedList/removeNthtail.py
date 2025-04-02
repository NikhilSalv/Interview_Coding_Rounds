class Node:
    def __init__(self,data, next_node=None):
        self.data = data
        self.next_node = next_node


def removenth_tail(head, N):
    fast = head
    slow = head

    for i in range(N):
        fast = fast.next_node
    
    while fast.next_node:
        slow = slow.next_node
        fast = fast.next_node
    print(slow.data)
    delNode = slow.next_node
    print("to be deleted : ", delNode.data)
    slow.next_node = slow.next_node.next_node
    return head


if __name__ == "__main__":
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    print(head.next_node.next_node.next_node.data)
    
    while head.next_node:
        print(head.data)
        head = head.next_node

    removenth_tail(head, 2)

    while head.next_node:
        print(head.data)
        head = head.next_node
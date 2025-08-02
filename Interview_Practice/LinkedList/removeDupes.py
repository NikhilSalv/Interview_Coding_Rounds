class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        # Detect duplicates
        if curr.next and curr.val == curr.next.val:
            # Skip all nodes with the same value
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            # Skip the last duplicate
            prev.next = curr.next
        else:
            # No duplicates; move prev
            prev = prev.next
        curr = curr.next

    return dummy.next

if __name__ == "__main__":
    head = Node(1)
    head.next_node = Node(1)
    head.next_node.next_node = Node(2)
    head.next_node.next_node.next_node = Node(2)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)

    result = deleteDuplicates(head)
    while result:
        print(result.val)
        result = result.next
    
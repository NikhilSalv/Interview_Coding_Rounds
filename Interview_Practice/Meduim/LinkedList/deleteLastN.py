
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNth(head, n):
    curr = head

    while n > 0:
        curr = curr.next
        print("current node : ", curr.val)
        n -= 1
    
    prev = head

    while curr.next:
        curr = curr.next
        prev = prev.next
    prev.next = prev.next.next
    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(2) # curr
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # 1 > 1 > 2 > 2 > 5 > 6
    # output :  1 > 1 > 2 > 5 > 6

    temp = head
    while temp:
        print(temp.val)
        temp = temp.next


    print("____________")


    result = deleteNth(head, 3)
    while result:
        print(result.val)
        result = result.next
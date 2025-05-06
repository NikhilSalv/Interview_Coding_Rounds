class ListNode:
    def __init__(self, data, next =None):
        self.data = data
        self.next = next


def ifCycle(head):

    slow = head.next
    fast = head.next.next

    while fast:
        if slow.data == fast.data:
            return True
        slow = slow.next
        fast = fast.next.next

    return False



if __name__ == "__main__":
    linkedList = ListNode(1)
    linkedList.next = ListNode(2)
    linkedList.next.next = ListNode(3)
    linkedList.next.next.next = ListNode(4)
    linkedList.next.next.next.next = ListNode(5)
    linkedList.next.next.next.next.next = ListNode(6)

    print(linkedList)

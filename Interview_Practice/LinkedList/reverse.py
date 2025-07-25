class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def linkedListToList(linkedList):
    outputList = []
    while linkedList:
        outputList.append(linkedList.val)
        linkedList = linkedList.next
    return outputList

def reverse(linkedList):
    current = linkedList
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

if __name__ == "__main__":
    l1 = [9,2,9,3,21,12,58,1]
    l1_ll = createLinkedList(l1)
    print(linkedListToList(reverse(l1_ll)))
"""
Given the LinkedList, and k, reverse the nodes of the linkedList in k groups. 

Solution link : https://youtu.be/YJrjUEhpmFk (Solved by Shikhar Chaudhary)
"""

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

def reverseNodesK(linkedList, k):
    head = linkedList
    len = 0
    if k == 1:
        return head
    while head.next:
        len += 1
        head = head.next
    len += 1
    head = linkedList

    if k > len:
        return linkedListToList(head)
    else:
        groups = len // k
        remaining =len % k
        print(groups, remaining)
        count = 0
        while count < groups:
            for _ in range(k):
                prev = None
                current = linkedList
                print(current.val)
                while current:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
            
            count += 1


if __name__ == "__main__":
    l1 = [9,2,9,3,21,12,58,1]
    l1_ll = createLinkedList(l1)
    # l2_ll = createLinkedList(l2)

    print(reverseNodesK(l1_ll,3))
"""
Given the head of a linked list, rotate the list to the right by k places.
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 0 or not head or not head.next:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k =  k % length

        if k == 0:
            return head

        new_tail = head
        new_end = length - k
        for _ in range(new_end - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
    


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4) # curr
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)


    temp = head
    while temp:
        print(temp.val)
        temp = temp.next


    print("____________")


    obj = Solution()
    result = obj.rotateRight(head, 3)
    while result:
        print(result.val)
        result = result.next
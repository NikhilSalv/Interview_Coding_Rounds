"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
# Definition for singly-linked list.
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


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        head = dummy
        carry = 0
        # total = 0
        while carry or l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1+ val2 + carry
            carry = total // 10
            digit = total % 10
            
            head.next = ListNode(digit)
            if l2 : l2 = l2.next
            if l1 : l1 = l1.next
            head = head.next

        return dummy.next


if __name__ == "__main__":
    l1 = [9,2,9,9,9,9,9]
    l2 = [9,9,9,9]
    l1_ll = createLinkedList(l1)
    l2_ll = createLinkedList(l2)
    # print(l1_ll.val)
    # print(l1_ll.next.val)
    add_obj = Solution()
    total_ll = add_obj.addTwoNumbers(l1_ll, l2_ll)
    while total_ll.next:
        print (total_ll.val, "\n")
        total_ll = total_ll.next
    print (total_ll.val)

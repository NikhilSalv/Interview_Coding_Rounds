class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        before_head = ListNode(0)
        prev_before = before_head
        after_head = ListNode(0)
        prev_after = after_head
        curr = head
        while curr:
            if curr.val < x:
                prev_before.next = curr
                prev_before = prev_before.next
            else:
                prev_after.next = curr
                prev_after = prev_after.next
            curr = curr.next
        if prev_after:
            prev_after.next = None
        tempafter = after_head
        tempbefore = before_head

        while tempbefore:
            print(tempbefore.val, "_____")
            tempbefore = tempbefore.next

        while tempafter:
            print(tempafter.val, "_____")
            tempafter = tempafter.next

        
        prev_before.next = after_head.next
        return before_head.next
    

if __name__ == "__main__":
        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2) # curr
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)

        temp = head
        while temp:
            print(temp.val)
            temp = temp.next


        print("____________")

        obj = Solution()
        result = obj.partition(head, 3)
        while result:
            print(result.val)
            result = result.next
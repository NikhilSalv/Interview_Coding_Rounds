"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        print("Current value : " , current.val)

        while list1 and list2:
            l1_val = list1.val
            l2_val = list2.val
            print(l1_val, l2_val,"Current value ", current.val)

            if l1_val < l2_val:
                current.next = list1
                list1 = list1.next
                # print(current.val, "Checking _____")
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy
            

if __name__ == "__main__":
    list1 = ListNode(4)
    list1.next = ListNode(17)
    list1.next.next = ListNode(34)
    list1.next.next.next = ListNode(56)
    list1.next.next.next.next = ListNode(77)
    list1.next.next.next.next.next = ListNode(600)


    list2 = ListNode(1)
    list2.next = ListNode(342)
    list2.next.next = ListNode(356)
    list2.next.next.next = ListNode(452)
    list2.next.next.next.next = ListNode(556)
    list2.next.next.next.next.next = ListNode(698)

    obj = Solution()
    mergedll = obj.mergeTwoLists(list1, list2)
    print(mergedll.val)






class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_A = 0
        len_B = 0
        dummy_a = headA
        dummy_b = headB

        while dummy_a:
            len_A += 1
            dummy_a = dummy_a.next
        while dummy_b:
            len_B += 1
            dummy_b = dummy_b.next

        diff = abs(len_A - len_B)
        pA = headA
        pB = headB
        if len_A > len_B:
            for _ in range(diff):
                pA = pA.next
        else:
            for _ in range(diff):
                pB = pB.next

        while pA != pB:
            pA = pA.next
            pB = pB.next
        
        return pA

if __name__ == "__main__":
    # Example usage:
    # Creating two intersecting linked lists for demonstration
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    # List A: 1 -> 2 \
    #                 -> 8 -> 9
    # List B:      3 /
    headA = ListNode(1)
    headA.next = ListNode(2)
    intersection = ListNode(8)
    headA.next.next = intersection
    intersection.next = ListNode(9)

    headB = ListNode(3)
    headB.next = intersection

    solution = Solution()
    intersect_node = solution.getIntersectionNode(headA, headB)
    if intersect_node:
        print(f"Intersected at node with value: {intersect_node.val}")
    else:
        print("No intersection")
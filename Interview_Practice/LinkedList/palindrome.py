class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

if __name__ == "__main__":
    # Example usage:
    # Creating a linked list for the palindrome 1 -> 2 -> 2 -> 1
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    palindrome_list = create_linked_list([1, 2, 2, 1])
    non_palindrome_list = create_linked_list([1, 2, 3])

    solution = Solution()
    print(solution.isPalindrome(palindrome_list))  # Output: True
    print(solution.isPalindrome(non_palindrome_list))  # Output: False
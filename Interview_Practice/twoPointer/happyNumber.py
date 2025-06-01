"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares 
of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

"""

class Solution(object):

    def next_digit(self,n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10
        return total

    def isHappy(self, n):
        slow = n
        fast = self.next_digit(n)
        while slow != fast and fast != 1:
            slow = self.next_digit(slow)
            fast = self.next_digit(self.next_digit(fast))
        return fast == 1
    

if __name__ == "__main__":
    obj = Solution()

    print(obj.isHappy(2))
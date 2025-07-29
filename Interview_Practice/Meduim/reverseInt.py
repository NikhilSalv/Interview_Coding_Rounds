"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution(object):
    def reverse(self, x):
        if 0 < x < 10:
            return x
        reversed = 0
        while x >= 1:
            last_digit = x % 10
            reversed = (reversed + last_digit) * 10
            x = x // 10
        return reversed // 10


if __name__ == "__main__":
    x = 1432
    print(Solution().reverse(x))
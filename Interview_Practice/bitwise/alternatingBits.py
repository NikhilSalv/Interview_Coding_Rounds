"""

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.


Example 1:

Input: n = 5

Output: true

Explanation: The binary representation of 5 is: 101


Example 2:

Input: n = 7

Output: false

Explanation: The binary representation of 7 is: 111.


Example 3:

Input: n = 11

Output: false

Explanation: The binary representation of 11 is: 1011.

"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        right_shifted = n >> 1
        # print(right_shifted)
        result = n ^ right_shifted
        # print(result & (result +1))
        return (result & (result +1)) == 0
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.hasAlternatingBits(5))  # True
    print(solution.hasAlternatingBits(7))  # False
    print(solution.hasAlternatingBits(11)) # False
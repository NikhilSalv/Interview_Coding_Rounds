"""
Problem Statement:

You are given a non-negative integer num and a positive integer k. Your task is to set the k-th bit of the binary representation of num to 1.

The binary representation of num is considered to have its rightmost bit as position 0.


Constraints:

0 ≤ num ≤ 10^9

0 <= k < 31

Input Format:

An integer num representing the given number.

An integer k representing the position of the bit to be set.




Output Format:

An integer representing the result after setting the k-th bit.




Examples:

1.

Input:

num = 5

k = 1

Output:

7

Explanation:

The binary representation of 5 is 101. Setting the 1st bit (from the right) results in 111, which is 7 in decimal.

"""

class Solution:
    def setBit(self, n: int, k: int) -> int:
        # print(1 << k)
        return n | (1 << k)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.setBit(10, 2))  # Example test case
    print(solution.setBit(15, 1))  # Example test case
    print(solution.setBit(0, 0))   # Example test case


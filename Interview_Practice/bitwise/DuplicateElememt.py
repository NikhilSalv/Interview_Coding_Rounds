"""
Given an array with 2n+1 integers, n elements appear twice in arbitrary places in the array and a single integer appears only once somewhere inside.

Write a program to find the single integer that appears only once.

Example 1

Input : { 1, 1, 2, 2, 3, 3, 4, 4, 5}

Output : 5

Reason :- All elements except 5 have exactly one duplicate
"""

class Solution:
    def missing_elements(self, arr):
        # n = int((len(arr) -1 ) / 2)
        # print(n)
        result =  0
        for i in arr:
            result = result ^ i
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.missing_elements([1, 2, 3, 2, 1]))  # Example test case
    print(solution.missing_elements([4, 5, 6, 5, 4, 7, 6]))  # Example test case
    print(solution.missing_elements([10, 20, 10, 30, 20, 40, 30]))  # Example test case
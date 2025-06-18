"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set(nums)
        longest = 0
        for n in nums:
            current = n
            length = 1
            if n - 1 not in visited:
                while current + 1 in visited:
                    length += 1
                    current += 1
                longest = max(length, longest)
        return longest

if __name__ == "__main__":
    nums = [5,8,6,7,100,4,200,1,3,2]
    obj = Solution()

    print(obj.longestConsecutive(nums))
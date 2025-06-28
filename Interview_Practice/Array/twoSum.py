class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:  # Only start if it's the beginning of a sequence
                current = n
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

            
if __name__ == "__main__":
    nums = [3,2,4] # Expected output [1,2]
    target = 6
    result = Solution()
    print(result.twoSum(nums,target))
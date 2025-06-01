"""
Given an array of positive integers nums and a positive integer target, 

return the minimal length of a subarray whose sum is greater than or equal to target. 

If there is no such subarray, return 0 instead.
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left_window = 0
        N = len(nums)
        min_len = float('inf')
        total = 0
        for right in range(N):
            total += nums[right]
            while total >= target:
                total -= nums[left_window]
                min_len = min(min_len,right-left_window +1)
                left_window += 1
        print("left : ", left_window - 1 , "right : ",right)
        return 0 if min_len == float('inf') else min_len
    
if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    target = 7
    obj = Solution()

    print(obj.minSubArrayLen(target,nums))
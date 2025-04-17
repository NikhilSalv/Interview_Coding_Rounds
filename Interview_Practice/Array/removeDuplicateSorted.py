"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
"""



class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        n = len(nums)
        for j in range(1,n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]  # Expected output 5
    result = Solution()
    print(result.removeDuplicates(nums))
    print(nums)

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) -1
        i = n -1
        while i >=0 and nums[i] >= nums[i+1]:
            i -=1
        if i == -1:
            print("its descending")
            print("nums:", nums)
            nums[:] = nums[::-1]
            print("reversed:", nums)
            return
        j = n
        while j>=0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        
 
if __name__ == "__main__":
    obj = Solution()
    nums = [5,2,1,7,3,2,1]
    print("Input: ", nums)
    obj.nextPermutation(nums)
    print("Output:", nums)






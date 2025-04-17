class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    nums = [3,2,2,3,4,5,6,7,3,3,1]  # Expected output 7
    k = 3
    result = Solution()
    print(result.removeElement(nums, k))
    print(nums)
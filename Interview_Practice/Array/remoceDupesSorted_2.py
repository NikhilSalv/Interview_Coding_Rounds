class Solution(object):
    def removeDuplicates(self, nums):
        i = 2
        n = len(nums)

        if n <=2:
            return n
        for j in range(2,n):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        print(nums[:i])
        return i

if __name__ == "__main__":
    nums = [1,1,1,1,1,1,2,3,4,4,6,6,6,6,6,7]  # Expected output 5
    num2 = [1,2,3]
    result = Solution()
    print(result.removeDuplicates(num2))
    print(num2)

class Solution(object):
    def majorityElement(self, nums):

        count = 0
        candidate = nums[0]

        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -=1
        return candidate

if __name__ == "__main__":
    nums = [2,2,2,2,2,3,4,4,6,6,6,2,2]  # Expected output 5
    result = Solution()
    print(result.majorityElement(nums))
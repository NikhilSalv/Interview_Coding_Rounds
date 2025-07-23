class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
            seen[nums[i]] = i
        return False
    
    def containsNearbyDuplicateEnumerate(self, nums, k):
        seen = {}

        for index, num in enumerate(nums):
            if num in seen:
                if index - seen[num] <= k:
                    return True
            else:
                seen[num] = index
        return False


if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    obj = Solution()
    print(obj.containsNearbyDuplicateEnumerate(nums,k))

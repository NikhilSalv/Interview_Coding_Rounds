class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
            seen[nums[i]] = i
        return False



if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 3
    obj = Solution()
    print(obj.containsNearbyDuplicate(nums,k))

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        N = len(nums)
        start = nums[0]
        for i in range(1,N):
            if nums[i] != nums[i-1] + 1:
                end = nums[i-1]
                if start == end:
                    result.append("{}".format(start))
                else:
                    result.append("{}->{}".format(start,end))
                start = nums[i]
        end = nums[-1]
        if start == end:
            result.append("{}".format(start))
        else:
            result.append("{}->{}".format(start,end))
        return result
    

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    obj = Solution()

    print(obj.summaryRanges(nums))
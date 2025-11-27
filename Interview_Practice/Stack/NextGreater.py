class Solution:
    def nextGreaterElements(self, nums):

        n = len(nums)
        res = [-1] * n
        stack = []  # store indices

        for i in range(2 * n):  # circular loop
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]

            if i < n:  # only push indices in the first pass
                stack.append(i)

        return res

if __name__ == "__main__":
    nums = [1,2,3,4,3]
    nums2 = [5,4,3,2,1]
    solution = Solution()
    print(solution.nextGreaterElements(nums2)) # Output: [2,3,4,-1,4]
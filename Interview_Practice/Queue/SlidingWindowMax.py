from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):

            # 1. Remove elements out of this window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. Add new index
            dq.append(i)

            # 4. Start adding results once first window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))  # Output: [3,3,5,5,6,7]
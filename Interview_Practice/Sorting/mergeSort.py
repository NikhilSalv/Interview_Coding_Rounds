class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        i = j = 0
        sorted_list = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        while i < len(left):
            sorted_list.append(left[i])
            i += 1
        while j < len(right):
            sorted_list.append(right[j])
            j += 1
        
        return sorted_list
    

if __name__ == "__main__":
    nums = [5,2,3,1]
    solution = Solution()
    print(solution.sortArray(nums))  # Output: [1,2,3,5]
    nums = [5,1,1,2,0,0]
    print(solution.sortArray(nums))  # Output: [0,0,1,1,2,5]
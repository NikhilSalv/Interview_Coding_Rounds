"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

def threeSum(arr):
    arr.sort()
    N = len(arr)
    output = []
    for i in range(N):
        left = i + 1
        right = N - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] == 0:
                output.append([arr[i] ,arr[left] , arr[right]])
                left += left
                right -= right
            elif arr[i] + arr[left] + arr[right] < 0:
                left += left
            else:
                right -= right
    return output


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
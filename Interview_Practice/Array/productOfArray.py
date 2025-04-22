"""
Product of Array except self
"""
def productOfArray(nums):
   n = len(nums)
   arr = [1] * n

   left_p, right_p = 1,1

   for i in range(n):
      arr[i] *= left_p
      left_p *= nums[i]
      
   for j in reversed(range(n)):
      arr[j] *= right_p
      right_p *= nums[j]

   return arr

if __name__ == "__main__":
   nums = [2, 3, 1, 1]
   print(productOfArray(nums))  # Output: [3,2,6,6]
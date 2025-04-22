def jump(nums):
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):  # We don't need to consider the last index
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps

if __name__ == "__main__":
   print(jump([2, 3, 1, 1, 4, 2, 1, 3, 7]))  # Output: 2
   string = [1,33,3,4]
   for i , c in enumerate(string):
       print(i, " ", c)
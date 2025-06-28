"""
Given an unsorted array arrl] of integers and an integer x,
find the floor and ceiling of x in arrIl.
Floor of x is the largest element which is smaller than or equal to x.
Floor of x doesn't exist if x is smaller than smallest element of arr [].
Ceil of x is the smallest element which is greater than or equal to x.
Ceil of x doesn't exist if x is greater than greatest element of arr|].
"""
def floor_ceil(nums, x):

    if not nums :
        return (-1,-1)
    
    floor = -float("inf")
    ceil = float("inf")

    for num in nums:
        if num <= x:
            floor = max(num, floor)
        if num >= x:
            ceil = min(ceil, num)
    return floor if floor != -float("inf") else -1, ceil if ceil != float("inf") else -1




if __name__ == "__main__":
    nums = [4,2,1,2,3,77,80]
    x = 81
    print(floor_ceil(nums, x))
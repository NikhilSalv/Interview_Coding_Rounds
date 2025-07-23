"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

"""
from datetime import datetime
import time

def time_analysis(func):
    def wrapper(*args, **kwrgs):
        print(f"arguments passed {args}, {kwrgs}")
        start_time = time.time()
        result = func(*args, **kwrgs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"elapsed time {total_time}")
        return result
    return wrapper

@time_analysis
def floor_ceil(nums, x, **kwrgs):

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
    # dictionary = {"name": " Nikhil", "age": 30}
    print(floor_ceil(nums, x, name='Nikhil', age=30, fsdjfk= 21))
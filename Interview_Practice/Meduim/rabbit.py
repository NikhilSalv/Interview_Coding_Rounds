"""
Problem Statement
medium
rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the 
answers in an integer array answers where answers[i] is the answer of the ith rabbit.
Given the array answers, return the minimum number of rabbits that could be in the forest.
Example 1:
Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "]" could both be
the same color, say red.
The rabbit that answered "2" can't be red or the
answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the
forest that didn't answer into the array.
The smallest possible number of rabbits in the
forest is therefore 5: 3 that answered plus 2 that
"""
from collections import Counter
import math
def minimum_groups(ans):
    groups = Counter(ans)
    total = 0
    for x , freq in groups.items():
        group_size = x+1
        number_of_groups = math.ceil(freq / group_size)
        total += number_of_groups * group_size
    return total


if __name__ == "__main__":
    answers = [1,1,1]
    print(minimum_groups(answers))



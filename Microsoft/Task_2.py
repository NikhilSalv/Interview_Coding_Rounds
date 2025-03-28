"""
A storeroom is used to organize items stored in it on N shelves. 
Shelves are numbered from 0 to N-1: The K-th shelf is dedicated to items of only one type, 
denoted by a positive integer A[k].

Recently it was decided that it is necessary to free R consecutive shelves. Shelves cannot be reordered. 
What is the maximum number of types of items which still can be stored in the storeroom 
after freeing R consecutive shelves?

Write a function:
    def solution(A, R)
that, given an array A of N integers representing types of items stored on storeroom shelves, 
and an integer R representing the number of consecutive shelves to be freed, 
returns the maximum number of different types of items that can be stored in the storeroom 
after freeing R consecutive shelves.

Examples:
1. Given A = [2, 1, 2, 3, 2, 2] and R = 3, your function should return 2. It
can be achieved, for example, by freeing shelves 2, 3 and 4 (shelves are numbered from 0).

2. Given A = [2, 3, 1, 1, 2] and R = 2, your function should return 3. All
three types can still be stored by freeing the last two shelves.

3. Given A = [20, 10, 10, 10, 30, 201 and R = 3, your function should return 3. 
It can be achieved by freeing the first three shelves.

4. Given A = [1, 100000, 1] and R = 3, your function should return O.
All the shelves need to be freed
"""

def solution(A, R):
    pass

if __name__ == "__main__":
    A = [2,1,2,3,2,2]
    R = 3
    result = solution(A, R)
    print(result)
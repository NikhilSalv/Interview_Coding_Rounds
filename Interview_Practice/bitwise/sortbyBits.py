"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]

Output: [0,1,2,4,8,3,5,6,7]

Explantion: [0] is the only integer with 0 bits.

[1,2,4,8] all have 1 bit.

[3,5,6] have 2 bits.

[7] has 3 bits.

The sorted array by bits is [0,1,2,4,8,3,5,6,7]

"""


class Solution:
    def sortByBits(self, arr):
        def count_bits(n):
            counter = 0
            while n > 0:
                if n & 1:
                    counter += 1
                n >>= 1
            return counter

        for i in range(len(arr)):
            for j in range(0, len(arr) - i -1):
                count_j = count_bits(arr[j])
                count_next = count_bits(arr[j+1])

                if count_j > count_next:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                elif count_j == count_next and arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortByBits([0,1,2,3,4,5,6,7,8]))  # Example test case
    print(solution.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))  # Example test case
    print(solution.sortByBits([10000,10000]))  # Example test case
    print(solution.sortByBits([2,3,5,7,11,13,17,19]))  # Example test case
    print(solution.sortByBits([10,100,1000,10000]))  # Example test case
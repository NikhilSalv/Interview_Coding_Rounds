from typing import List

class Solution:
    def total_swaps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Step 1: Create a sorted version of the array
        sorted_arr = sorted(arr)
        
        # Step 2: Map each element to its correct index in the sorted array
        originalIndex = {num: i for i, num in enumerate(sorted_arr)}
        
        visited = [False] * n  # Keep track of visited elements
        swaps = 0
        
        # Step 3: Traverse the array to find cycles
        for i in range(n):
            # If element is already visited or in correct position, skip
            if visited[i] or originalIndex[arr[i]] == i:
                continue
            
            cycle_size = 0
            j = i
            
            # Count the size of the cycle
            while not visited[j]:
                visited[j] = True
                j = originalIndex[arr[j]]  # Move to the index where this element should be
                cycle_size += 1
            
            # If cycle size > 0, we need (cycle_size - 1) swaps
            if cycle_size > 0:
                swaps += (cycle_size - 1)
        
        return swaps


if __name__ == "__main__":
    sol = Solution()
    arr1 = [4, 3, 1, 2]
    print(sol.total_swaps(arr1))  # Expected output: 3

    # arr2 = [1, 5, 4, 3, 2]
    # print(sol.total_swaps(arr2))  # Expected output: 2

    # arr3 = [2, 3, 4, 1, 5]
    # print(sol.total_swaps(arr3))  # Expected output: 3

    # arr4 = [1, 2, 3, 4, 5]
    # print(sol.total_swaps(arr4))  # Expected output: 0
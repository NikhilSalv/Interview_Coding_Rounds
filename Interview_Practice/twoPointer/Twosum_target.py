"""
You are given an integer array nums and an integer target. Return indices of the two numbers such that they add up to target.

Approach :

* Clarify the problem statement :
- So, there will be two input parameters, a list of integers, and an integer target. correct?
- The objective is to find out two numbers only, which will add up to the target

* Discuss the edge cases
- there will be multiple possibilities in the list which will add up to the target or just one?
- What if there are such cases? What the output should look like?
- What if the list is empty?

* Discuss the brute force approach :
 > Aknowledge inefficiency / time complexity

 - There is a brute force approch I can think of, such that, I will iterate over the array using for loop from left to right
 - In each iteration, I will check each pair of elements and compare that with the target.
 Will return the indexes if found. 
 - Since there will be nested loops, the time complexity is of order of O(n^2). Due to this, this approach is inefficient.
 

* Optimise step by step
 > Identify the pattern
 > if stuck discuss possible optimisations
 - I will use hash map technique to store the visited element in the list and its index.
 - in each iteration, the difference between target and current element could be found.
 - This difference will be checked in the hash map, if it exists.
 - - if it does, then return its index and the index of the current element in the loop.


* Confirm the approach
- With this approach, the time complexity will be O(N). Hence, efficient than the fbruteforce. 
- Shall I go ahead with this approach?

* Implement solution

def find_sum_elememts(arr, target):
    N = len(arr)

    if not arr:
        print("String is empty")
        return -1
    
    visited = {}

    for i in range(0 ,N):
        diff = target - arr[i]
        print(diff)

        if diff in visited.keys():
            return [visited[diff], i]
        visited[arr[i]] = i
        print(visited)
    return -1


* Analyse time  complexity
- The function iterates through the array once → O(N).
- Each dictionary operation (lookup and insertion) runs in O(1) on average.
- Since we only traverse the array once and perform constant-time operations in each iteration, the overall time complexity is O(N).
- Best Case (Early Return)
> If a valid pair is found early (e.g., at index i=1), the function returns immediately.
> In this case, the time complexity is O(1) to O(N), depending on how early the pair is found.
- Worst Case
If the pair is found at the last index or does not exist, the loop runs for all N elements.
This results in O(N) complexity.

* Analyse space complexity

- A dictionary (visited) is used to store seen values and their indices.
- In the worst case, the dictionary stores all N elements of the array.
- Dictionary storage requires O(N) space.

- Best Case (Early Return)
> If a pair is found early, the dictionary stores only a few elements → O(1) space.

- Worst Case
> If no valid pair exists, all N elements are stored in visited → O(N) space.

* Run through edge cases
- Edge case if the list is empyt is implemented.


"""
def find_sum_elememts(arr, target):
    N = len(arr)

    if not arr:
        print("String is empty")
        return -1
    
    visited = {}

    for i in range(0 ,N):
        diff = target - arr[i]

        if diff in visited:
            return [visited[diff], i]
        visited[arr[i]] = i
    return -1

def find_sum_elememts_optimal(arr, target):
    N = len(arr)
    left = 0
    right = N - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return -1
    
if __name__ == "__main__":
    target = 62
    arr = [1,3,6,7,8,54,77,85]
    print(find_sum_elememts_optimal(arr, target))
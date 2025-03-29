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


* Analyse time and space complexity
- 

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
    
if __name__ == "__main__":
    target = 5
    arr = [1,3,6,1,7,8,0,77,54,2]
    print(find_sum_elememts(arr, target))
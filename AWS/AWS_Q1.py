"""
Given an array of integers, create a 2-dimensional array where the first element is a distinct value 
from the array and the second element is that value's frequency within the array. 
Sort the resulting array descending by frequency. If multiple values have the same frequency,
they should be sorted ascending.
"""

def sortArray(arr):
    """
    This function takes an array and creates a 2D list with element and its frequency,
    sorted descending by frequency and ascending by element for equal frequencies.
    """
    # Create a dictionary to store the count of each number
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Sort the numbers based on frequency (descending) and then by value (ascending)
    sorted_nums = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    
    # Format the output as requested
    return [[num, count] for num, count in sorted_nums]

def main():
    # Example arrays
    arr1 = [4, 3, 5, 3, 1, 2, 1, 4, 3, 5, 7, 7, 7, 7, 7]
    arr2 = [1, 1, 2, 3, 3]

    result1 = sortArray(arr1)
    result2 = sortArray(arr2)
    
    print("Frequency Array 1:", result1)
    print("Frequency Array 2:", result2)

if __name__ == "__main__":
    main()

"""
Given an array of integers, create a 2-dimensional array where the first element is a distinct value 
from the array and the second element is that value's frequency within the array. 
Sort the resulting array descending by frequency. If multiple values have the same frequency,
they should be sorted ascending.
"""

def sortArray(arr):
    """
    This function takes an array and creates 2D list with element and its frequency
    """
    freq = []

    for i in set(arr):
        freq.append([i, arr.count(i)])
        
    result = sortByFreq_and_element(freq) 
    return result



def sortByFreq_and_element(arr):

    """
    This function takes a 2D array created in sortArray() function, 
    and sorts in Descending order by frequency, 
    and also, if the frequency if same, the elemets are sorted in ascending order
    """

    sorted_by_freq = sorted(arr, key=lambda x : (-x[1], x[0]))
    return sorted_by_freq

def main():
    # Example array
    arr = [4, 3, 5, 3, 1, 2, 1, 4, 3, 5,7,7,7,7,7]

    result = sortArray(arr)
    print("Frequency Array:", result)

if "__main__" == __name__:
    main()

"""
Given a list of strings made up of the characters 'a' and 'b', 
create a regular expression that will
match strings that begin and end with the same
letter.


Example : 
'a', 'aa', and 'bababbb' match.
'ab'and 'baba' do not match.
"""
def frequency_sort(arr):
    # Count the frequency of each number
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Create a 2D array of [value, frequency] pairs
    result = [[num, freq] for num, freq in frequency.items()]
    
    # Sort the result: first by frequency (descending), then by value (ascending)
    result.sort(key=lambda x: (-x[1], x[0]))
    
    return result

# Example usage
arr = [3, 3, 1, 2, 1]
print(frequency_sort(arr))  # Output: [[3, 2], [1, 2], [2, 1]]

"""
I approached this problem by breaking it down into several steps.

Walkthrough my thought process:
First, I realized I needed to count how many times each number appears in the array. I decided to use a dictionary for this because it gives me quick lookup and update times. I called this dictionary frequency.
Next, I needed to create the 2D array the question asked for. I did this by turning my frequency dictionary into a list of lists, where each inner list contains a number and how many times it appears.
The tricky part was the sorting. The question wanted the results sorted in a specific way: first by frequency (highest to lowest), and then by the actual number (lowest to highest) if the frequencies were the same.
To handle this, I used Python's sort method with a custom key. The key is a lambda function that returns a tuple: (-x[1], x[0]). Here's why I did this:

x[1] is the frequency. I put a minus sign in front of it because I want to sort frequencies from highest to lowest.
x[0] is the number itself. This comes second in the tuple, so it only matters when frequencies are equal.

Python sorts tuples by comparing their elements in order, so this gives me exactly the sorting behavior I need.
Finally, I just return this sorted list, and that's my solution!

I tested it with the example input [3, 3, 1, 2, 1], and it gave me [[1, 2], [3, 2], [2, 1]], which is correct: 1 and 3 both appear twice, but 1 comes first because it's smaller, and 2 appears once so it comes last.
This solution should work efficiently for most inputs, but if you're dealing with extremely large arrays, you might need to consider more optimized approaches. 
"""
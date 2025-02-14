'''Given an array of integers numbers, compare the sum of elements on even positions against the sum of elements on odd positions (o -based). 
Return "even" if the sum of elements on even positions is greater,
"odd" if the sum of elements on odd positions is greater, or "equal" if both sums are equal.
Note: You are not expected to provide the most optimal solution, 
but a solution with time complexity not worse than O (numbers. length?) will fit within the execution time limit.'''

'''
Example
• For numbers = 11, 2, 3, 4, 51, the output should be solution (numbers) = "even" .

Explanation:
• Sum of elements on even positions is 1 + 3 + 5 = 9.
• Sum of elements on odd positions is 2 + 4 = 6 .
• 9 > 6, the expected output is "even"
• For numbers = [-1, 4, 3, -2], the output should be solution (numbers) = "equal"

Explanation:
• Sum of elements on even positions is (-1) + 3 = 2.
• Sum of elements on odd positions is 4 + (-2) = 2 .
• 2 = 2, so the expected output is "equal" .
'''
def Solutio(array):
  even_sum = sum(array[0::2])
  odd_sum = sum(array[1::2])
  return "even" if even_sum > odd_sum else "odd" if even_sum < odd_sum else "equal"


if __name__ == "__main__":
  numbers = [10,3,41,4,50,5]
  print(Solution(numbers))

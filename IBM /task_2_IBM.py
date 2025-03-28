"""
In securities research, an analyst will look at a number of attributes for a stock. 
One analyst would like to keep a record of the highest positive spread between 
a closing price and the closing price on any prior day in history.
Determine the maximum positive spread for a stock given its price history.
If the stock remains flat or declines for the full period, return -1

Example 0
px = [7, 1, 2, 5]
Calculate the positive difference between each price and its predecessors:
• At the first quote, there is no earlier quote to compare to.
• At the second quote, there was no earlier price that was lower.
• At the third quote, the price is higher than the second quote:
0 2-1=1
• For the fourth quote, the price is higher than the third and the second quotes:
• 5-2=3
0 5-1=4
• The maximum difference is 4.

Example 1
px = [7, 5, 3, 1]

• The price declines each quote, so there is never a difference greater than 0. In this case, return -1.
Function Description
Complete the function maxDifference in the editor below.
maxDifference has the following parameters:
int px/n]: an array of stock prices (quotes)

Returns:
int: the maximum difference between two prices as described above
"""

def maxDifference (px):

    pass


if __name__ == "__main__":
    pass
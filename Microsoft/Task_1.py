"""
A game board has a row of N+1 fields, numbered from 0 to N from left to right. One letter ("a" or "b') is written between every two adjacent fields.
Letters on the board are described by a string L of length N, where LIK] (for K within the range [O..N-1]) is the letter between fields K and K+1.
For example, given L = "aaabab" and N,= 6 the game board at the
beginning will look like this:
  |     |a|      |a|      |a|       |b|       |a|       |b|       |

There is a game piece standing on some field on the board. It can move one field to the left or to the right, 
passing over one of the letters. 
The letter over which the game piece passes switches to the opposite one (a" becomes "b" and "b" becomes "a*). 
The game piece can move multiple times, so letters may also be switched multiple times.
For above example, if the game piece stood on the field number 3 and then moved to the left,
the game board would look like the picture below:

"""

def is_balanced(L_string):
    pass

def solution(L, start):

    N = len(L)

    pass


if __name__ == "__main__":
    L = "aaabab"
    start = 3
    result = solution(L, start)
    print(result)
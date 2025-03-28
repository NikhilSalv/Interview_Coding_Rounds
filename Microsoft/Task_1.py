"""
A game board has a row of N+1 fields, numbered from 0 to N from left to right. One letter ("a" or "b') is written between every two adjacent fields.
Letters on the board are described by a string L of length N, where L[K] (for K within the range [O..N-1]) is the letter between fields K and K+1.
For example, given L = "aaabab" and N,= 6 the game board at the beginning will look like this:

  |     |a|      |a|      |a|       |b|       |a|       |b|       |

There is a game piece standing on some field on the board. It can move one field to the left or to the right, 
passing over one of the letters. 
The letter over which the game piece passes switches to the opposite one (a" becomes "b" and "b" becomes "a"). 
The game piece can move multiple times, so letters may also be switched multiple times.
For above example, if the game piece stood on the field number 3 and then moved to the left,
the game board would look like the picture below:

"""

def is_balanced(L_string):
    return L_string.count("a") == L_string.count("b")

def solution(L, start):

    N = len(L)

    if N % 2 != 0:
        return -2
    
    if is_balanced(L):
        return 0
    
    queue = [(start, L, 0)]
    visited_position = set()

    while queue:
        position, current_L, move = queue.pop(0)

        for new_position in [position + 1, position - 1]:
            if 0 <= new_position < N +1:
                flip_idx = min(position, new_position)

                if 0 <= flip_idx < N:
                    print(f"Current L {current_L}")
                    print(f"Flipping at {flip_idx}")
                    new_L = current_L[:flip_idx] + ('b' if current_L[flip_idx] == 'a' else 'a') + current_L[flip_idx + 1:]
                    print(f"Flipped new_L {new_L}")
                    if is_balanced(new_L):
                        return move +1
                    
                if (new_position, new_L) not in visited_position:
                    visited_position.add((new_position, new_L))
                    queue.append((new_position, new_L, move +1))
    return -1


if __name__ == "__main__":
    L = "aaaasssa"
    start = 3
    result = solution(L, start)
    print(result)
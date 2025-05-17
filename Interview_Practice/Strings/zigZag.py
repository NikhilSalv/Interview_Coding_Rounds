
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

Output 'PAHNAPLSIIGYIR'

"""


def zigZag(s, n):
    rows = ["" for _ in range(n)]
    N = len(s)
    curr_row = 0
    direction = False

    for i in range(N):
        rows[curr_row] += s[i]
        if curr_row == 0 or curr_row == n -1:
            direction = not direction
        curr_row += 1 if direction else -1

    return "".join(rows)



if __name__ == "__main__":
    s = "PAYPALISHIRING"
    print(zigZag(s,3))

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
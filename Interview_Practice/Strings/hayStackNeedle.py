


def hayStackNeedle(h,n):
    for i in range(len(h) - len(n) + 1):
        if h[i: i+ len(n)] == n:
            return i
    return -1

if __name__ == "__main__":
    h = "butsad"
    n = "sad"
    print(hayStackNeedle(h,n))
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1


if __name__ == "__main__":
    nums = count_up_to(10**9)  # Generator created, uses almost no memory!
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))





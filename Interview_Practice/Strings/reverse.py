def reverse(string):
    # print((string[4]))
    print(" ".join(string.split()[::-1]))
    # print(" ".join(s))
    # for i in range(len(string) -1, -1, -1):
    #     print(string[i], end = " ")


if __name__ == "__main__":
    string = "reverse this string and print"
    reverse(string)
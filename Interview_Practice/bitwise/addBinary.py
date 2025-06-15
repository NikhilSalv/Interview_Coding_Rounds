
def addBinary(a,b):
    if len(b) > len(a):
        a,b = b,a
    a= list(a)
    b= list(b)
    carry = 0
    b= ["0"] * (len(a) - len(b)) + b
    result = []

    for i in range(len(a) -1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        carry = total // 2
        result.append(str(total % 2))
    if carry == 1:
        result.append("1")
    return "".join(reversed(result))



if __name__ == "__main__":
    a = "11010101"
    b = "111111111111"
    print(addBinary(a,b))
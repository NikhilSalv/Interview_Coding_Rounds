def print_subarray(arr, length):
    """Function to print all the subarrays given in an array
    Input arr--> array, length -->length of an array """
    i = 0
    while i < length:
        j = i
        while j < length:
            k = i
            while k <= j:
                print(arr[k], end = "")
                k += 1
            j += 1
            print("")
        i += 1
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print_subarray(arr, n)


if __name__ == "__main__":
    main()